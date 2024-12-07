import subprocess


def main_test(file_path, test_name):
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
    print(test_name, ":", "SUCCESS")


def test_big_text():
    file_path = "cat/tests/big_text"
    main_test(file_path, "big test")


def test_case_b():
    file_path = "cat/tests/case_b"
    main_test(file_path, "case b")


def test_case_e():
    file_path = "cat/tests/case_e"
    main_test(file_path, "case e")


def test_case_n():
    file_path = "cat/tests/case_n"
    main_test(file_path, "case n")


def test_case_s():
    file_path = "cat/tests/case_s"
    main_test(file_path, "case_s")


def test_case_t():
    file_path = "cat/tests/case_t"
    main_test(file_path, "case t")


def test_case_upE():
    file_path = "cat/tests/case_upE"
    main_test(file_path, "case E")


def test_case_upT():
    file_path = "cat/tests/case_upT"
    main_test(file_path, "case T")


def test_hard_case():
    file_path = "cat/tests/hard_case"
    main_test(file_path, "hard case")


def test_memory_case():
    file_path = "cat/tests/memory_case"
    main_test(file_path, "memory overflow test")


def test_case_new():
    file_path = "cat/tests/new"
    main_test(file_path, "new test")


def test_case_nonprint():
    file_path = "cat/tests/nonprint"
    main_test(file_path, "nonprint symbols test")

