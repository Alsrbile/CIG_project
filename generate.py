from CIG_project.generate_func import generate_SDXL_images


if __name__ == '__main__':
    
    prompts = [
        "A photo of a cute dog sitting in the beach",
        "A photo of a cute dog standing in the snow",
        "A photo of a cute dog running in the park"
    ]
    
    concept_token = "dog"
    
    output_dir = "output"
                
    generate_SDXL_images(prompts=prompts, concept_token=concept_token, output_dir='output')