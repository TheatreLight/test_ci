import subprocess


def test_one_file_one_pattern():
    result_original = subprocess.run(
        ['grep', "coronavirus", "grep/grep_tests/new"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', "coronavirus", "grep/grep_tests/new"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print("one_file_one_pattern", ":", "SUCCESS")


def test_seven_files_one_pattern():
    result_original = subprocess.run(
        ['grep', "a", "grep/grep_tests/new", "grep/grep_tests/old",
         "grep/grep_tests/18_test_pat", "grep/grep_tests/19_test_pat",
         "grep/grep_tests/forgrep", "grep/grep_tests/pattern", "grep/grep_tests/text"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', "a", "grep/grep_tests/new", "grep/grep_tests/old",
         "grep/grep_tests/18_test_pat", "grep/grep_tests/19_test_pat",
         "grep/grep_tests/forgrep", "grep/grep_tests/pattern", "grep/grep_tests/text"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print("seven_files_one_pattern", ":", "SUCCESS")


def test_e_two_patterns_one_file():
    result_original = subprocess.run(
        ['grep', "-e", "all", "-e", "it", "grep/grep_tests/new"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', "-e", "all", "-e", "it", "grep/grep_tests/new"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print("e_test_two_patterns_one_file", ":", "SUCCESS")


def test_e_two_patterns_two_files():
    result_original = subprocess.run(
        ['grep', "-e", "all", "-e", "it", "grep/grep_tests/new", "grep/grep_tests/old"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', "-e", "all", "-e", "it", "grep/grep_tests/new", "grep/grep_tests/old"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print("e_test_two_patterns_two_files", ":", "SUCCESS")


def test_i_one_pattern_one_file():
    result_original = subprocess.run(
        ['grep', "-i", "health", "grep/grep_tests/new"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', "-i", "health", "grep/grep_tests/new"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print("i_test_one_pattern_one_file", ":", "SUCCESS")


def test_i_two_patterns_two_files():
    result_original = subprocess.run(
        ['grep', "-i", "health", "-e", "grep/grep_tests/new", "grep/grep_tests/old"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', "-i", "health", "-e", "grep/grep_tests/new", "grep/grep_tests/old"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print("i_test_two_patterns_two_files", ":", "SUCCESS")


def test_v_one_pattern_one_file():
    result_original = subprocess.run(
        ['grep', "-v", "health", "grep/grep_tests/new"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', "-v", "health", "grep/grep_tests/new"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print("v_test_one_pattern_one_file", ":", "SUCCESS")


def test_v_two_patterns_two_files():
    result_original = subprocess.run(
        ['grep', "-ve", "health", "-e", "grep", "grep/grep_tests/new", "grep/grep_tests/old"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', "-ve", "health", "-e", "grep", "grep/grep_tests/new", "grep/grep_tests/old"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print("v_test_two_patterns_two_files", ":", "SUCCESS")


def test_c_one_pattern_one_file():
    result_original = subprocess.run(
        ['grep', "-c", "health", "grep/grep_tests/new"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', "-c", "health", "grep/grep_tests/new"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print("c_test_one_pattern_one_file", ":", "SUCCESS")


def test_c_two_patterns_two_files():
    result_original = subprocess.run(
        ['grep', "-ce", "health", "-e", "grep", "grep/grep_tests/new", "grep/grep_tests/old"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', "-ce", "health", "-e", "grep", "grep/grep_tests/new", "grep/grep_tests/old"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print("ce_test_two_patterns_two_files", ":", "SUCCESS")


def test_l_one_pattern_one_file():
    result_original = subprocess.run(
        ['grep', "-l", "health", "grep/grep_tests/new"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', "-l", "health", "grep/grep_tests/new"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print("l_test_one_pattern_one_file", ":", "SUCCESS")


def test_l_two_patterns_two_files():
    result_original = subprocess.run(
        ['grep', "-le", "health", "-e", "grep", "grep/grep_tests/new", "grep/grep_tests/old"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', "-le", "health", "-e", "grep", "grep/grep_tests/new", "grep/grep_tests/old"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print("le_test_two_patterns_two_files", ":", "SUCCESS")


def test_n_one_pattern_one_file():
    result_original = subprocess.run(
        ['grep', "-n", "health", "grep/grep_tests/new"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', "-n", "health", "grep/grep_tests/new"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print("n_test_one_pattern_one_file", ":", "SUCCESS")


def test_n_two_patterns_two_files():
    result_original = subprocess.run(
        ['grep', "-ne", "health", "-e", "grep", "grep/grep_tests/new", "grep/grep_tests/old"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    result_current = subprocess.run(
        ['./grep/s21_grep', "-ne", "health", "-e", "grep", "grep/grep_tests/new", "grep/grep_tests/old"],
        stdout=subprocess.PIPE,
        text=True
    ).stdout

    assert result_current == result_original, "FAIL"
    print("ne_test_two_patterns_two_files", ":", "SUCCESS")
