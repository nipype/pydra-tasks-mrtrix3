import typing  # noqa: F401
import numpy.typing
from fileformats.core import extra_implementation
from fileformats.medimage import DwiEncoding
from fileformats.medimage.diffusion import EncodingArrayType
from fileformats.vendor.mrtrix3.medimage import BFile, ImageFormatWithDwiEncoding


@extra_implementation(DwiEncoding.read_encodings)
def bfile_read_array(
    bfile: BFile,
) -> EncodingArrayType:
    return numpy.asarray(
        [[float(x) for x in ln.split()] for ln in bfile.read_contents().splitlines()]
    )


@extra_implementation(DwiEncoding.read_encodings)
def image_format_with_dwi_encoding_read_array(
    image_with_dwi: ImageFormatWithDwiEncoding,
) -> EncodingArrayType:
    return image_with_dwi.metadata["encodings"]
