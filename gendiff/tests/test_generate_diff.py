from gendiff.modules.generate_diff import generate_diff
import pytest

fixtures_dir = "gendiff/tests/fixtures/"
# general func job
normal = ((f"{fixtures_dir}file1.json",
          f"{fixtures_dir}file2.json"),
          f"{fixtures_dir}expected_result.txt")
# files are similar
same = ((f"{fixtures_dir}file1.json",
        f"{fixtures_dir}file1.json"),
        f"{fixtures_dir}result_same.txt")
# one file is empty
one_empty = ((f"{fixtures_dir}file1.json",
             f"{fixtures_dir}empty_file.json"),
             f"{fixtures_dir}/result_one_empty.txt")
# both files are empty
both_empty = ((f"{fixtures_dir}empty_file.json",
              f"{fixtures_dir}empty_file.json"),
              f"{fixtures_dir}result_both_empty.txt")


@pytest.mark.parametrize("test_input,result",
                         [normal, same, one_empty, both_empty])
def test_generate_diff(test_input, result):
    file_1, file_2 = test_input
    assert generate_diff(file_1, file_2) == open(result).read()
