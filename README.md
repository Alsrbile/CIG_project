# Consistent image generation project

![이미지 설명](results.png)
![이미지 설명](https://github.com/Alsrbile/CIG_project/blob/main/results.png?raw=true)


## 설명
이 코드는 `generate.py` 파일 내부에서 generate_SDXL_images 함수를 통해 영상을 생성합니다.

generate_SDXL_images 함수 인자
- **`prompts`**: 캐릭터를 묘사하는 텍스트 프롬프트 (ex: 'A photo of a cute dog sitting in the beach')
- **`concept_token`**: 캐릭터 지정 (ex: 'dog')
- **`output_dir`**: 생성 이미지 저장 경로 지정

- 본 코드는 Stable Diffusion XL를 사용했습니다.
  
## 환경 설정
```bash
conda env create --file environment.yml
```

## 실행 예시
generate.py 내부 prompts, concept_token, output_dir 변경 후,
```bash
python generate.py
```



