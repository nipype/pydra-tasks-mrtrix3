import gzip

import pytest
from fileformats.medimage import (
    DicomDir,
    NiftiBvec,
    NiftiGzBvec,
    NiftiGzXBvec,
    NiftiXBvec,
)
from fileformats.vendor.mrtrix3.medimage import ImageFormat, ImageFormatGz, ImageHeader


# @pytest.mark.xfail(reason="not sure what the reason is at this stage, might be bug in Pydra")
def test_nifti_to_mrtrix(dummy_dwi_dicom):
    nifti_fsgrad = NiftiBvec.convert(dummy_dwi_dicom)
    ImageFormat.convert(nifti_fsgrad)
    ImageHeader.convert(nifti_fsgrad)


def test_dicom_to_mrtrix_image(dummy_dwi_dicom):
    ImageFormat.convert(dummy_dwi_dicom)


def test_dicom_to_mrtrix_image_header(dummy_dwi_dicom):
    ImageHeader.convert(dummy_dwi_dicom)


def test_mif_to_mifgz(dummy_nifti):
    mif = ImageFormat.convert(dummy_nifti)
    mif_gz = ImageFormatGz.convert(mif)
    ImageFormat.convert(mif_gz)


def _read_mrtrix_header(image: ImageFormat | ImageFormatGz | ImageHeader) -> list[str]:
    """The lines of the text header of an MRtrix image, up to the 'END' line"""
    opener = gzip.open if isinstance(image, ImageFormatGz) else open
    lines = []
    with opener(image.fspath, "rb") as f:
        for raw in f:
            line = raw.decode("latin-1").rstrip("\n")
            if line == "END":
                break
            lines.append(line)
    return lines


@pytest.fixture(
    scope="module", params=[NiftiBvec, NiftiGzBvec, NiftiXBvec, NiftiGzXBvec]
)
def nifti_fslgrad(
    request: pytest.FixtureRequest, dummy_dwi_dicom: DicomDir
) -> NiftiBvec | NiftiGzBvec | NiftiXBvec | NiftiGzXBvec:
    return request.param.convert(dummy_dwi_dicom)  # type: ignore[no-any-return]


@pytest.mark.parametrize("target", [ImageFormat, ImageFormatGz, ImageHeader])
def test_nifti_fslgrad_to_mrtrix(
    nifti_fslgrad: NiftiBvec | NiftiGzBvec | NiftiXBvec | NiftiGzXBvec,
    target: type[ImageFormat | ImageFormatGz | ImageHeader],
) -> None:
    """The FSL-style gradients in the .bvec/.bval side-cars of a NIfTI image are
    embedded in the header of the converted MRtrix image, as its 'dw_scheme'"""
    converted = target.convert(nifti_fslgrad)
    assert isinstance(converted, target)

    header = _read_mrtrix_header(converted)
    dw_scheme = [
        [float(v) for v in ln.split(":", 1)[1].split(",")]
        for ln in header
        if ln.startswith("dw_scheme:")
    ]
    b_values = [
        float(b)
        for b in nifti_fslgrad.encoding.b_values_file.fspath.read_text().split()
    ]
    assert len(dw_scheme) == len(b_values)
    assert all(len(row) == 4 for row in dw_scheme)
    # The directions may be reoriented from image to scanner space, but the b-values
    # are carried over as they are
    assert [row[3] for row in dw_scheme] == pytest.approx(b_values)
