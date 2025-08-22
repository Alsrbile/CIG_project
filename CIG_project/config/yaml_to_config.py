import yaml
import argparse

def has_nested_attr(obj, attr_path):
    attrs = attr_path.split('.')
    for attr in attrs:
        if hasattr(obj, attr):
            obj = getattr(obj, attr)
        else:
            return False
    return True

def update_config(config, args):
    def _update_arg(name):
        if has_nested_attr(config, name):
            return True
        else:
            return False

    # Environment
    if _update_arg('Environment.seed'):
        args.seed = config.Environment.seed
    if _update_arg('Environment.device'):
        args.device = config.Environment.device
    
    # Inference
    if _update_arg('Inference.guidance_scale'):
        args.guidance_scale = config.Inference.guidance_scale
    if _update_arg('Inference.num_inference_steps'):
        args.num_inference_steps = config.Inference.num_inference_steps
    if _update_arg('Inference.mask_dropout'):
        args.mask_dropout = config.Inference.mask_dropout
    
    # Path
    if _update_arg('Path.pretrained_model'):
        args.pretrained_model = config.Path.pretrained_model
    if _update_arg('Path.mask_dropout'):
        args.output_dir = config.Path.output_dir
    if _update_arg('Path.single_benchmark_dir'):
        args.single_benchmark_dir = config.Path.single_benchmark_dir
    

    return args

def load_yaml_config(yaml_file):
    with open(yaml_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def dict_to_namespace(config_dict):
    namespace = argparse.Namespace()
    for key, value in config_dict.items():
        if isinstance(value, dict):
            setattr(namespace, key, dict_to_namespace(value))
        elif isinstance(value, list):
            setattr(namespace, key, value)
        else:
            setattr(namespace, key, value)
    return namespace
