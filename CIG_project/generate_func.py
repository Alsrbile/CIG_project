# import sys
# import os

# # CIG_project 디렉토리를 Python 경로에 추가
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
import os
import torch
import argparse

from .src.module.sdxl_pipeline import CustomStableDiffusionXLPipeline
from .src.module.mask_dropout import create_token_indices

from .config.yaml_to_config import load_yaml_config, dict_to_namespace, update_config

YAML_PATH = "CIG_project/config/configs.yaml"



def generate_SDXL_images(prompts, concept_token, output_dir):
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    
    config_dict = load_yaml_config(YAML_PATH)
    config = dict_to_namespace(config_dict)
    update_config(config, args)
    
    custom_pipeline = CustomStableDiffusionXLPipeline.from_pretrained(
        args.pretrained_model,
        torch_dtype=torch.float16,
        variant="fp16",
        use_safetensors=True,
    ).to(args.device)

    generator = torch.Generator(device=args.device).manual_seed(args.seed)
    
    custom_pipeline.enable_freeu(s1=0.6, s2=0.4, b1=1.1, b2=1.2)
    tokenizer = custom_pipeline.tokenizer
    
    batch_size = len(prompts)
    token_indices = create_token_indices(prompts, batch_size, concept_token, tokenizer)
    
    attention_store_kwargs = {
                    'token_indices': token_indices,
                    'mask_dropout': args.mask_dropout,
                }
    
    result = custom_pipeline(prompts, generator=generator,
                                 num_inference_steps=args.num_inference_steps, 
                                 guidance_scale=args.guidance_scale,
                                 attention_store_kwargs=attention_store_kwargs,
                )


    # output_subdir = os.path.join(output_dir, f"{i}")
    os.makedirs(output_dir, exist_ok=True)
    
    for j, image in enumerate(result.images):
        image_path = os.path.join(output_dir, f"{prompts[j]}.png")
        image.save(image_path)
      
