import subprocess

def test_my_cat():
    file_path = "../cat/tests/big_text"

    result_original = subprocess.run(
        ['cat', file_path],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_my_cat = subprocess.run(
        ['./cat/s21_cat', file_path],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_my_cat == result_original, "FAIL"
