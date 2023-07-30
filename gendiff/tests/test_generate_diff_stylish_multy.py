from gendiff.modules.generate_difference import generate_diff
import pytest

# multilevel
json_dir = "gendiff/tests/fixtures/multilevel/json/"
yaml_dir = "gendiff/tests/fixtures/multilevel/yaml/"
txt_dir = "gendiff/tests/fixtures/multilevel/"
# test json files
# general func job
mul_normal = ((f"{json_dir}file1.json", f"{json_dir}file2.json"),
              f"{txt_dir}expected_result.txt")
# one file is empty
mul_one_empty = ((f"{json_dir}file1.json", f"{json_dir}empty_file.json"),
                 f"{txt_dir}/result_one_empty.txt")
# both files are empty
mul_both_empty = ((f"{json_dir}empty_file.json", f"{json_dir}empty_file.json"),
                  f"{txt_dir}result_both_empty.txt")

# test yaml files
# general func job
mul_normal_yml = ((f"{yaml_dir}file1.yaml", f"{yaml_dir}file2.yaml"),
                  f"{txt_dir}expected_result.txt")
# one file is empty
mul_one_empty_yml = ((f"{yaml_dir}file1.yaml", f"{yaml_dir}empty_file.yaml"),
                     f"{txt_dir}/result_one_empty.txt")
# both files are empty
mul_both_empty_yml = ((f"{yaml_dir}empty_file.yaml",
                       f"{yaml_dir}empty_file.yaml"),
                      f"{txt_dir}result_both_empty.txt")

# test json & yaml files
mul_normal_json_yml = ((f"{yaml_dir}file1.yaml", f"{json_dir}file2.json"),
                       f"{txt_dir}expected_result.txt")


@pytest.mark.parametrize("test_input,result",
                         [mul_normal, mul_one_empty, mul_both_empty,
                          mul_normal_yml, mul_one_empty_yml, mul_both_empty_yml,
                          mul_normal_json_yml])
def test_generate_diff_mul(test_input, result):
    file_1, file_2 = test_input
    assert generate_diff(file_1, file_2) == open(result).read()
