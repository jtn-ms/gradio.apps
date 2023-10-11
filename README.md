# gradio.apps

## source

- chatbot
  * [ ] [GPT4Tools](https://github.com/AILab-CVC/GPT4Tools)

- face
  * [x] [deepface](https://github.com/serengil/deepface): vgg-face
  * [x] [face_recognition](https://github.com/ageitgey/face_recognition)
  * [x] [inswapper](https://github.com/haofanwang/inswapper.git)
  * [x] [refacer](https://github.com/jtn-ms/refacer.git)

- super resolution
  * [x] [CodeFormer](https://github.com/sczhou/CodeFormer.git): face

- audio
  * [ ] [speechbrain](https://github.com/speechbrain/speechbrain)
  * [ ] [transformers](https://github.com/huggingface/transformers)

- ocr
  * [x] paddleOCR
  * [x] tesseractOCR
  * [x] pororoOCR
  * [x] [chineseOCR](https://github.com/YCG09/chinese_ocr): detection(ctpn) + recognition(DenseNet + CTC)
  * [x] [cnOCR](https://github.com/breezedeus/CnOCR): PyTorch/MXNet
  * [x] [HyperLPR](https://github.com/szad670401/HyperLPR): Keras

- vehicle
  * [ ] ssd

- video
  * [x] [moviepy](https://github.com/Zulko/moviepy)
  * [x] [videogrep](https://github.com/antiboredom/videogrep)
  * [x] [vosk - video transcribe](https://github.com/alphacep/vosk-api.git)
  * [ ] [backgroundremover](https://github.com/nadermx/backgroundremover): no library supported, just command-line tool
  * [x] [rembg](https://github.com/danielgatis/rembg)

- video + speech recognition
  * [ ] [Video2Description](https://github.com/scopeInfinity/Video2Description)

- Translator
  * [ ] [Korean-English-translator](https://github.com/virsagothethird/Korean-English-translator.git)
  * [ ] Chatgpt-based [Koalpaca-Translation-KR2EN](https://github.com/gyupro/Koalpaca-Translation-KR2EN)
  * [x] Chatgpt-based [zh2en](https://huggingface.co/Helsinki-NLP/opus-mt-zh-en?text=%E6%88%91%E4%B8%8D%E7%9F%A5%E9%81%93%E4%BD%A0%E5%9C%A8%E8%AF%B4%E4%BB%80%E4%B9%88)
  * [ ] Chatgpt-based [ko2en](https://huggingface.co/Helsinki-NLP/opus-mt-ko-en?text=%EC%96%B8%EC%A0%9C+%EB%B0%A5%EB%A8%B9%EC%9E%94%3F)

- Text2Image
  * [ ] [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0?text=a+photo+of+an+astronaut+riding+a+horse+on+mars)

- Image2Image
  - [ ] [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0)

- Speech2Text
  * [ ] https://github.com/openai/whisper

- Text2Speech
  * [ ] https://github.com/suno-ai/bark

## Models

- overview: https://platform.openai.com/docs/models/overview
- whisper - speech2text: https://github.com/openai/whisper.git
- https://huggingface.co/models?pipeline_tag=translation&sort=downloads
- https://huggingface.co/models?sort=downloads

## Articles

- https://github.com/christianversloot/machine-learning-articles
- https://huggingface.co/docs/transformers/pipeline_tutorial

## Docker Images

| name | base | content
| ---- | ---- | -------
| llama2-webui | py3 | llama2 - chatbot & code completion
| speechbrain  | py3 | text2speech, speech2text
| refacer | py3 |refacer-face swap, inswapper-face swap, codeformer - face restoration
| ocr | py3 | facerecognition - rec/det, cnocr - chn, paddleocr - all, pororoocr - ko/en
| ssd | py2 | chinese_ocr, hyplr-1(chinese license plat recognition), surveillance, vehicle insurance
| nvm | py3 | base image
| opencv3 | py2 | base image
| py3 | | base image
| py2 | | base image
| mongo | | base image

## py3 only

- tensorflow2
- gradio

## Utils

### clean cache

```sh
pip cache purge
apt clean

make clean


docker volume ls
docker builder prune -a
docker container prune
docker image prune -a
docker volume prune
docker system prune -all

# forfiles /s /m *.vhdx /c "cmd /c echo @fsize @path"
# Get-ChildItem -Recurse -Filter *.vhdx | Measure-Object -Property Length -Sum | ForEach-Object { $_.Sum / 1MB }
find /cygdrive/c/Users -type f -name \*.vhdx -exec du -ah {} \;
# find /cygdrive/c/Users -name "*.vhdx" -exec du -ah {} \; | sort -h
# find /cygdrive/c/Users -name \*.vhdx "%p\t%k KB\n"
# find /cygdrive/c/Users -type f -exec ls -lh \{\} \;
# find /cygdrive/c/Users -type f -exec wc -c \{\} \;

wsl -l -v
wsl --shutdown

diskpart
> select vdisk file="C:\Users\username\AppData\Local\Docker\wsl\data\ext4.vhdx"
> compact vdisk

Enable-WindowsOptionalFeature -Online -FeatureName $("Microsoft-Hyper-V", "Containers") -All
& 'C:\Program Files\Docker\Docker\DockerCli.exe' -SwitchDaemon
```