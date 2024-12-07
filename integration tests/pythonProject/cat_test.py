import subprocess

def main_test(file_path):
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

def test_big_text():
    file_path = "cat/tests/big_text"
    main_test(file_path)

def test_case_b():
    file_path = "cat/tests/case_b"
    main_test(file_path)
    
def test_case_e():
    file_path = "cat/tests/case_e"