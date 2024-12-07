import subprocess


def main_test(pattern, file, test_name):
    command = pattern + " " + file
    print(command)
    result_original = subprocess.run(
        ['grep', pattern, file],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', command],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print(test_name, ":", "SUCCESS")


def test_one_file_one_pattern():
    main_test(" coronavirus ", "grep_tests/new", "one_file_one_pattern")


def test_seven_files_one_pattern():
    main_test("a",
              "grep_tests/new grep_tests/old grep_tests/18_test_pat grep_tests/19_test_pat grep_tests/forgrep "
              "grep_tests/pattern grep_tests/text",
              "seven_files_one_pattern")


def test_e_two_patterns_one_file():
    main_test("-e all -e it", "grep_tests/new", "e_test_two_patterns_one_file")


def test_e_two_patterns_two_files():
    main_test("-e all -e it", "grep_tests/new grep_tests/old", "e_test_two_patterns_two_files")


def test_i_one_pattern_one_file():
    main_test("-i health", "grep_tests/new", "i_test_one_pattern_one_file")


def test_i_two_patterns_two_files():
    main_test("-ie health -e grep", "grep_tests/new grep_tests/old", "i_test_two_patterns_two_files")


def test_v_one_pattern_one_file():
    main_test("-v health", "grep_tests/new", "v_test_one_pattern_one_file")


def test_v_two_patterns_two_files():
    main_test("-ve health -e grep", "grep_tests/new grep_tests/old", "v_test_two_patterns_two_files")


def test_c_one_pattern_one_file():
    main_test("-c health", "grep_tests/new", "c_test_one_pattern_one_file")


def test_c_two_patterns_two_files():
    main_test("-ce health -e grep", "grep_tests/new grep_tests/old", "c_test_two_patterns_two_files")


def test_l_one_pattern_one_file():
    main_test("-l health", "grep_tests/new", "l_test_one_pattern_one_file")


def test_l_two_patterns_two_files():
    main_test("-le health -e grep", "grep_tests/new grep_tests/old", "l_test_two_patterns_two_files")


def test_n_one_pattern_one_file():
    main_test("-n health", "grep_tests/new", "n_test_one_pattern_one_file")


def test_n_two_patterns_two_files():
    main_test("-ne health -e grep", "grep_tests/new grep_tests/old", "n_test_two_patterns_two_files")
