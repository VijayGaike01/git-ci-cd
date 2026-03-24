import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.app import analyze_logs


def test_log_counts(tmp_path):
    # Create a temporary log file
    log_file = tmp_path / "test.log"
    log_file.write_text(
        "INFO: Start\nERROR: Fail\nINFO: Continue\n"
    )

    # Capture output
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output

    analyze_logs(str(log_file))

    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()

    assert "INFO count: 2" in output
    assert "ERROR count: 1" in output