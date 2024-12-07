import subprocess


def main_test(pattern, file, test_name):
    command = pattern + " " + file
    result_original = subprocess.run(
        ['grep', command],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_my_cat = subprocess.run(
        ['./grep/s21_grep', command],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_my_cat == result_original, "FAIL"
    print(test_name, ":", "SUCCESS")


def one_file_one_pattern_test():
    main_test("coronavirus", "grep_tests/new", "one_file_one_pattern")


def seven_files_one_pattern_test():
    main_test("a",
              "grep_tests/new grep_tests/old grep_tests/18_test_pat grep_tests/19_test_pat grep_tests/forgrep grep_tests/pattern grep_tests/text",
              "seven_files_one_pattern")


def e_test_two_patterns_one_file_test():
    main_test("-e all -e it", "grep_tests/new", "e_test_two_patterns_one_file")


def e_test_two_patterns_two_files_test():
    main_test("-e all -e it", "grep_tests/new grep_tests/old", "e_test_two_patterns_two_files")


def i_test_one_pattern_one_file_test():
    main_test("-i health", "grep_tests/new", "i_test_one_pattern_one_file")


def i_test_two_patterns_two_files_test():
    main_test("-ie health -e grep", "grep_tests/new grep_tests/old", "i_test_two_patterns_two_files")


def v_test_one_pattern_one_file_test():
    main_test("-v health", "grep_tests/new", "v_test_one_pattern_one_file")


def v_test_two_patterns_two_files_test():
    main_test("-ve health -e grep", "grep_tests/new grep_tests/old", "v_test_two_patterns_two_files")


def c_test_one_pattern_one_file_test():
    main_test("-c health", "grep_tests/new", "c_test_one_pattern_one_file")


def c_test_two_patterns_two_files_test():
    main_test("-ce health -e grep", "grep_tests/new grep_tests/old", "c_test_two_patterns_two_files")


def l_test_one_pattern_one_file_test():
    main_test("-l health", "grep_tests/new", "l_test_one_pattern_one_file")


def l_test_two_patterns_two_files_test():
    main_test("-le health -e grep", "grep_tests/new grep_tests/old", "l_test_two_patterns_two_files")


def n_test_one_pattern_one_file_test():
    main_test("-n health", "grep_tests/new", "n_test_one_pattern_one_file")


def n_test_two_patterns_two_files_test():
    main_test("-ne health -e grep", "grep_tests/new grep_tests/old", "n_test_two_patterns_two_files")