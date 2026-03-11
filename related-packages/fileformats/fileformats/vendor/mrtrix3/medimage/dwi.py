from fileformats.core import validated_property, extra_implementation
from fileformats.core.mixin import WithAdjacentFiles
from fileformats.medimage import DwiEncoding, Nifti1, NiftiGz, NiftiX, NiftiGzX, Dwi
from fileformats.medimage.diffusion import EncodingArrayType
from .image import ImageFormat, ImageHeader, ImageFormatGz


class BFile(DwiEncoding):
    """MRtrix-style diffusion encoding, all in one file"""

    ext = ".b"


class ImageFormatWithDwiEncoding(DwiEncoding, ImageFormat[Dwi]):
    pass


# NIfTI file format gzipped with BIDS side car
class WithBFile(DwiEncoding, WithAdjacentFiles):
    @validated_property
    def encoding(self) -> BFile:
        return BFile(self.select_by_ext(BFile))  # noqa


class NiftiB(WithBFile, Nifti1):
    iana_mime = "application/x-nifti2+b"


class NiftiGzB(WithBFile, NiftiGz):
    iana_mime = "application/x-nifti2+gzip.b"


class NiftiXB(WithBFile, NiftiX):
    iana_mime = "application/x-nifti2+json.b"


class NiftiGzXB(WithBFile, NiftiGzX):
    iana_mime = "application/x-nifti2+gzip.json.b"


class ImageFormatB(WithBFile, ImageFormat):
    iana_mime = "application/x-mrtrix-image-format.b"


class ImageFormatGzB(WithBFile, ImageFormatGz):
    iana_mime = "application/x-mrtrix-image-format+gzip.b"


class ImageHeaderB(WithBFile, ImageHeader):
    iana_mime = "application/x-mrtrix-image-header.b"


@extra_implementation(DwiEncoding.read_encodings)
def with_b_file_read_array(with_b_file: WithBFile) -> EncodingArrayType:
    return with_b_file.encoding.read_encodings()
