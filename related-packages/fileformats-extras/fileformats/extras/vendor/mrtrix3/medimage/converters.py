import itertools
import typing as ty
from pathlib import Path

from fileformats.core import FileSet, converter
from fileformats.medimage import (
    Bval,
    Bvec,
    MedicalImage,
    NiftiBvec,
    NiftiGzBvec,
    NiftiGzXBvec,
    NiftiXBvec,
)
from fileformats.vendor.mrtrix3.medimage import (
    ImageFormat as MrtrixImage,
)
from fileformats.vendor.mrtrix3.medimage import (
    ImageFormatGz as MrtrixImageGz,
)
from fileformats.vendor.mrtrix3.medimage import (
    ImageHeader as MrtrixImageHeader,
)
from pydra.compose import python, workflow

from pydra.tasks.mrtrix3.v3_1 import MrConvert

MRTRIX_FORMATS = (MrtrixImage, MrtrixImageGz, MrtrixImageHeader)

# NIfTI images with FSL-style diffusion gradients in .bvec/.bval side-cars
NIFTI_FSLGRAD_FORMATS = (NiftiBvec, NiftiGzBvec, NiftiXBvec, NiftiGzXBvec)
NiftiFslGrad = NiftiBvec | NiftiGzBvec | NiftiXBvec | NiftiGzXBvec

T = ty.TypeVar("T")


def out_file_template(fileformat: type[FileSet]) -> str:
    """Return the output file name for a given file format

    Parameters
    ----------
    fileformat : type
        the file format class

    Returns
    -------
    str
        the output file name
    """
    return "out" + fileformat.ext


def converters(
    sources: ty.Iterable[type[FileSet]], targets: ty.Iterable[type[FileSet]]
) -> ty.Callable[[T], T]:
    """Decorator that registers a task as the converter between every pair of the
    source and target formats, setting the name of its output file from the extension
    of the target

    Parameters
    ----------
    sources : Iterable[type[FileSet]]
        the formats to convert from
    targets : Iterable[type[FileSet]]
        the formats to convert to
    """

    def decorator(task: T) -> T:
        for source, target in itertools.product(sources, targets):
            converter(
                source_format=source,
                target_format=target,
                out_file_=out_file_template(target),
            )(task)
        return task

    return decorator


# Any medical image can be converted to the MRtrix formats with mrconvert
converters(sources=[MedicalImage], targets=MRTRIX_FORMATS)(MrConvert)


@python.define(outputs=["fslgrad"])
def ExtractFslGrad(in_file: NiftiFslGrad) -> tuple[Bvec, Bval]:
    """The .bvec and .bval side-cars of the image, in the order mrconvert's -fslgrad
    option takes them"""
    return in_file.encoding, in_file.encoding.b_values_file


@converters(sources=NIFTI_FSLGRAD_FORMATS, targets=MRTRIX_FORMATS)
@workflow.define(outputs=["out_file"])
def MrConvertWithFslGrad(
    in_file: NiftiFslGrad,
    out_file: Path,
) -> MrtrixImage | MrtrixImageGz | MrtrixImageHeader:
    """Converts a NIfTI image to an MRtrix format, embedding its FSL-style diffusion
    gradients in the header of the converted image (as its 'dw_scheme')"""

    extract_fslgrad = workflow.add(ExtractFslGrad(in_file=in_file))

    mrconvert = workflow.add(
        MrConvert(in_file=in_file, fslgrad=extract_fslgrad.fslgrad, out_file=out_file)
    )

    return mrconvert.out_file  # type: ignore[no-any-return]
