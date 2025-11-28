# Auto-generated test for peaksconvert

import pytest
from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.vendor.mrtrix3.medimage import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_1 import PeaksConvert


@pytest.mark.xfail
def test_peaksconvert(tmp_path, cli_parse_only):

    task = PeaksConvert(
        debug=False,
        force=False,
        in_file=Nifti1.sample(),
        in_format=None,
        in_reference=None,
        out_format=None,
        out_reference=None,
        out_file=File.sample(),
    )
    result = task(worker="debug")
    assert not result.errored
