"""
load all confings in neox/configs in order to perform validations implemented in NeoXArgs 
"""
import pytest
import yaml
from ..common import get_configs_with_path

def run_neox_args_load_test(yaml_files):
    from megatron.neox_arguments import NeoXArgs

    yaml_list = get_configs_with_path(yaml_files)
    args_loaded = NeoXArgs.from_ymls(yaml_list)
    assert isinstance(args_loaded, NeoXArgs)

    # initialize an empty config dictionary to be filled by yamls
    config = dict()

    # iterate of all to be loaded yaml files
    for conf_file_name in yaml_list:

        # load file
        with open(conf_file_name) as conf_file:
            conf = yaml.load(conf_file, Loader=yaml.FullLoader)

        # check for key duplicates and load values
        for conf_key, conf_value in conf.items():
            if conf_key in config:
                raise ValueError(
                    f'Conf file {conf_file_name} has the following duplicate keys with previously loaded file: {conf_key}')

            conf_key_converted = conf_key.replace("-", "_")  # TODO remove replace and update configuration files?
            config[conf_key_converted] = conf_value

    # validate that neox args has the same value as specified in the config (if specified in the config)
    for k, v in config.items():
        neox_args_value = getattr(args_loaded, k)
        assert v == neox_args_value, "loaded neox args value "+str(k)+" == "+str(neox_args_value)+" different from config file "+str(v)

@pytest.mark.cpu 
def test_neoxargs_load_arguments_small_local_setup():
    """
    verify small.yml can be loaded without raising validation errors
    """
    run_neox_args_load_test(["small.yml", "local_setup.yml"])

@pytest.mark.cpu 
def test_neoxargs_load_arguments_small_local_setup_text_generation():
    """
    verify small.yml can be loaded together with text generation without raising validation errors
    """
    run_neox_args_load_test(["small.yml", "local_setup.yml", "text_generation.yml"])

@pytest.mark.cpu     
def test_neoxargs_load_arguments_medium_local_setup():
    """
    verify medium.yml can be loaded without raising validation errors
    """
    run_neox_args_load_test(["medium.yml", "local_setup.yml"])

@pytest.mark.cpu 
def test_neoxargs_load_arguments_large_local_setup():
    """
    verify large.yml can be loaded without raising validation errors
    """
    run_neox_args_load_test(["large.yml", "local_setup.yml"])

@pytest.mark.cpu 
def test_neoxargs_load_arguments_2_7B_local_setup():
    """
    verify 2-7B.yml can be loaded without raising validation errors
    """
    run_neox_args_load_test(["2-7B.yml", "local_setup.yml"])

@pytest.mark.cpu 
def test_neoxargs_load_arguments_6_7B_local_setup():
    """
    verify 6-7B.yml can be loaded without raising validation errors
    """
    run_neox_args_load_test(["6-7B.yml", "local_setup.yml"])

@pytest.mark.cpu 
def test_neoxargs_load_arguments_13B_local_setup():
    """
    verify 13B.yml can be loaded without raising validation errors
    """
    run_neox_args_load_test(["13B.yml", "local_setup.yml"])

@pytest.mark.cpu 
def test_neoxargs_load_arguments_XL_local_setup():
    """
    verify XL.yml can be loaded without raising validation errors
    """
    run_neox_args_load_test(["XL.yml", "local_setup.yml"])

@pytest.mark.cpu 
def test_neoxargs_load_arguments_175B_local_setup():
    """
    verify 13B.yml can be loaded without raising validation errors
    """
    run_neox_args_load_test(["175B.yml", "local_setup.yml"])

@pytest.mark.cpu 
def test_neoxargs_fail_instantiate_without_required_params():
    """
    verify assertion error if required arguments are not provided
    """
    
    try:
        run_neox_args_load_test(["local_setup.yml"])
        assert False
    except Exception as e:
        assert True

@pytest.mark.cpu 
def test_neoxargs_fail_instantiate_without_any_params():
    """
    verify assertion error if required arguments are not provided
    """
    from megatron.neox_arguments import NeoXArgs
    
    try:
        args_loaded = NeoXArgs()
        assert False
    except Exception as e:
        assert True
