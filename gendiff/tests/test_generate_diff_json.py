from gendiff.modules.generate_difference import generate_diff
import pytest

# multilevel plain
json_dir = "gendiff/tests/fixtures/multilevel/json/"
yaml_dir = "gendiff/tests/fixtures/multilevel/yaml/"
txt_dir = "gendiff/tests/fixtures/multilevel/"
# test json files
# general func job
json_normal = ((f"{json_dir}file1.json", f"{json_dir}file2.json"),
               f"{txt_dir}expected_result_json.txt")

# test yaml files
# general func job
json_normal_yml = ((f"{yaml_dir}file1.yaml", f"{yaml_dir}file2.yaml"),
                   f"{txt_dir}expected_result_json.txt")

# test json & yaml files
json_normal_json_yml = ((f"{yaml_dir}file1.yaml", f"{json_dir}file2.json"),
                        f"{txt_dir}expected_result_json.txt")


@pytest.mark.parametrize("test_input,result",
                         [json_normal, json_normal_yml,
                          json_normal_json_yml])
def test_generate_diff_json(test_input, result):
    file_1, file_2 = test_input
    assert generate_diff(file_1, file_2, "json") == open(result).read()
