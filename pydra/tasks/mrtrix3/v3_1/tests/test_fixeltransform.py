# Auto-generated test for fixeltransform

import pytest
from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.vendor.mrtrix3.medimage import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_1 import FixelTransform


@pytest.mark.xfail
def test_fixeltransform(tmp_path, cli_parse_only):

    task = FixelTransform(
        debug=False,
        fixel_in=File.sample(),
        force=False,
        warp=Nifti1.sample(),
        fixel_out=File.sample(),
    )
    result = task(worker="debug")
    assert not result.errored
