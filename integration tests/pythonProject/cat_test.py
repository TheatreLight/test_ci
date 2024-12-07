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
    main_test(file_path)

def test_case_n():
    file_path = "cat/tests/case_n"
    main_test(file_path)

def test_case_s():
    file_path = "cat/tests/case_s"
    main_test(file_path)

def test_case_t():
    file_path = "cat/tests/case_t"
    main_test(file_path)

def test_case_upE():
    file_path = "cat/tests/case_upE"
    main_test(file_path)

def test_case_upT():
    file_path = "cat/tests/case_upT"
    main_test(file_path)

def test_hard_case():
    file_path = "cat/tests/hard_case"
    main_test(file_path)

def test_memory_case():
    file_path = "cat/tests/memory_case"
    main_test(file_path)

def test_case_new():
    file_path = "cat/tests/new"
    main_test(file_path)

def test_case_nonprint():
    file_path = "cat/tests/nonprint"
    main_test(file_path)

def test_orig_case_b():
    file_path = "cat/tests/orig_case_b"
    main_test(file_path)

def test_orig_case_e():
    file_path = "cat/tests/orig_case_e"
    main_test(file_path)

def test_orig_case_n():
    file_path = "cat/tests/orig_case_n"
    main_test(file_path)

def test_orig_case_s():
    file_path = "cat/tests/orig_case_s"
    main_test(file_path)

def test_orig_case_t():
    file_path = "cat/tests/orig_case_t"
    main_test(file_path)

def test_case_out3():
    file_path = "cat/tests/out3"
    main_test(file_path)

def test_out4():
    file_path = "cat/tests/out4"
    main_test(file_path)