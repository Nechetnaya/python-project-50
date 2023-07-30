from gendiff.gendiff import generate_diff
import pytest

# multilevel plain
json_dir = "gendiff/tests/fixtures/multilevel/json/"
yaml_dir = "gendiff/tests/fixtures/multilevel/yaml/"
txt_dir = "gendiff/tests/fixtures/multilevel/"
# test json files
# general func job
plain_normal = ((f"{json_dir}file1.json", f"{json_dir}file2.json"),
                f"{txt_dir}expected_result_plain.txt")

# test yaml files
# general func job
plain_normal_yml = ((f"{yaml_dir}file1.yaml", f"{yaml_dir}file2.yaml"),
                    f"{txt_dir}expected_result_plain.txt")

# test json & yaml files
plain_normal_json_yml = ((f"{yaml_dir}file1.yaml", f"{json_dir}file2.json"),
                         f"{txt_dir}expected_result_plain.txt")


@pytest.mark.parametrize("test_input,result",
                         [plain_normal, plain_normal_yml,
                          plain_normal_json_yml])
def test_generate_diff_plain(test_input, result):
    file_1, file_2 = test_input
    assert generate_diff(file_1, file_2, "plain") == open(result).read()
