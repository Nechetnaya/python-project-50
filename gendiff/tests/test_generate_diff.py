from gendiff.modules.generate_diff import generate_diff


def test_generate_diff():
    result = open("gendiff/tests/fixtures/expected_result.txt").read()
    assert generate_diff("gendiff/tests/fixtures/file1.json",
                         "gendiff/tests/fixtures/file2.json") == result


def test_generate_diff_same():
    result = open("gendiff/tests/fixtures/result_same.txt").read()
    assert generate_diff("gendiff/tests/fixtures/file1.json",
                         "gendiff/tests/fixtures/file1.json") == result


def test_generate_diff_one_empty():
    result = open("gendiff/tests/fixtures/result_one_empty.txt").read()
    assert generate_diff("gendiff/tests/fixtures/file1.json",
                         "gendiff/tests/fixtures/empty_file.json") == result


def test_generate_diff_both_empty():
    result = open("gendiff/tests/fixtures/result_both_empty.txt").read()
    assert generate_diff("gendiff/tests/fixtures/empty_file.json",
                         "gendiff/tests/fixtures/empty_file.json") == result
