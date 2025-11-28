# Auto-generated test for fixelfilter

import pytest
from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.vendor.mrtrix3.medimage import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_1 import FixelFilter


@pytest.mark.xfail(reason="Job fixelfilter is known not pass yet")
@pytest.mark.xfail
def test_fixelfilter(tmp_path, cli_parse_only):

    task = FixelFilter(
        cfe_c=None,
        cfe_dh=None,
        cfe_e=None,
        cfe_h=None,
        cfe_legacy=False,
        debug=False,
        filter="cfe",
        force=False,
        fwhm=None,
        in_file=File.sample(),
        mask=None,
        matrix=File.sample(),
        minweight=None,
        threshold_connectivity=None,
        threshold_value=None,
        out_file=File.sample(),
    )
    result = task(worker="debug")
    assert not result.errored
