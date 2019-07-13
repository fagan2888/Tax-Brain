import shutil
from pathlib import Path
from taxbrain import report


def test_report(tb_static):
    """
    Ensure that all report files are created
    """
    outdir = "testreform"
    name = "Test Report"
    report(
        tb_static, name=name, outdir=outdir
    )
    dir_path = Path(outdir)
    assert dir_path.exists()
    assert Path(dir_path, "Test-Report.md").exists()
    assert Path(dir_path, "Test-Report.pdf").exists()
    assert Path(dir_path, "Test-Report.html").exists()
    diff_png = Path(dir_path, "difference_graph.png")
    diff_svg = Path(dir_path, "difference_graph.svg")
    assert diff_png.exists() or diff_svg.exists()
    dist_png = Path(dir_path, "dist_graph.png")
    dist_svg = Path(dir_path, "dist_graph.svg")
    assert dist_png.exists() or dist_svg.exists()
    shutil.rmtree(dir_path)
