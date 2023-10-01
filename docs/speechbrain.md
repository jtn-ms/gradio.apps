### [Text2Speech](https://huggingface.co/speechbrain/tts-tacotron2-ljspeech)

- access container
```bash
$ make access.bash
```

- copy model and hyperparams.yaml 
```sh
root@758fcb2265f5:/app/speechbrain# mkdir tmpdir
root@758fcb2265f5:/app/speechbrain# copy /models/tts-tacotron2-ljspeech/model.ckpt /tmpdir
```

```python
from speechbrain.pretrained import Tacotron2
tacotron2 = Tacotron2.from_hparams(source="speechbrain/TTS_Tacotron2", savedir="tmpdir")
items = [
       "A quick brown fox jumped over the lazy dog",
       "How much wood would a woodchuck chuck?",
       "Never odd or even"
     ]
mel_outputs, mel_lengths, alignments = tacotron2.encode_batch(items)
```

```python
import torchaudio
from speechbrain.pretrained import Tacotron2
from speechbrain.pretrained import HIFIGAN

# Intialize TTS (tacotron2) and Vocoder (HiFIGAN)
tacotron2 = Tacotron2.from_hparams(source="speechbrain/tts-tacotron2-ljspeech", savedir="tmpdir_tts")
hifi_gan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-ljspeech", savedir="tmpdir_vocoder")

# Running the TTS
mel_output, mel_length, alignment = tacotron2.encode_text("Mary had a little lamb")

# Running Vocoder (spectrogram-to-waveform)
waveforms = hifi_gan.decode_batch(mel_output)

# Save the waverform
torchaudio.save('example_TTS.wav',waveforms.squeeze(1), 22050)
```

```sh
root@758fcb2265f5:/app/speechbrain# find . -name model.ckpt
root@758fcb2265f5:/app/speechbrain# find . -name hyperparams.yaml
./tests/integration/ASR_CTC/hyperparams.yaml      
...
./tmpdir/hyperparams.yaml
./tmpdir_tts/hyperparams.yaml
./tmpdir_vocoder/hyperparams.yaml
```

```sh
docker cp speechbrain-app:/app/speechbrain/example_TTS.wav .
```

### [Speech2Text](https://huggingface.co/speechbrain/asr-transformer-transformerlm-librispeech)

```python
from speechbrain.pretrained import EncoderDecoderASR

asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-transformer-transformerlm-librispeech", savedir="pretrained_models/asr-transformer-transformerlm-librispeech")
asr_model.transcribe_file("speechbrain/asr-transformer-transformerlm-librispeech/example.wav")
```

```sh
docker cp ./example_TTS.wav speechbrain-app:/app/speechbrain/
```

```python
asr_model.transcribe_file("example_TTS.wav")
```
#### [common-en](https://huggingface.co/speechbrain/asr-wav2vec2-commonvoice-en)

```python
from speechbrain.pretrained import EncoderDecoderASR

asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-wav2vec2-commonvoice-en", savedir="pretrained_models/asr-wav2vec2-commonvoice-en")
asr_model.transcribe_file("speechbrain/asr-wav2vec2-commonvoice-en/example.wav")

```

#### [Mandarin](https://huggingface.co/speechbrain/asr-wav2vec2-transformer-aishell)

```python
from speechbrain.pretrained import EncoderDecoderASR
asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-wav2vec2-transformer-aishell", savedir="pretrained_models/asr-wav2vec2-transformer-aishell")
asr_model.transcribe_file("speechbrain/asr-wav2vec2-transformer-aishell/example_mandarin.wav")
```

### [Speaker Recognition](https://huggingface.co/speechbrain/spkrec-ecapa-voxceleb)

```python
from speechbrain.pretrained import SpeakerRecognition
verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")
score, prediction = verification.verify_files("tests/samples/ASR/spk1_snt1.wav", "tests/samples/ASR/spk2_snt1.wav") # Different Speakers
score, prediction = verification.verify_files("tests/samples/ASR/spk1_snt1.wav", "tests/samples/ASR/spk1_snt2.wav") # Same Speaker
```

### [Language Detection](https://huggingface.co/speechbrain/lang-id-commonlanguage_ecapa)

```python
import torchaudio
from speechbrain.pretrained import EncoderClassifier
classifier = EncoderClassifier.from_hparams(source="speechbrain/lang-id-commonlanguage_ecapa", savedir="pretrained_models/lang-id-commonlanguage_ecapa")
# Italian Example
out_prob, score, index, text_lab = classifier.classify_file('speechbrain/lang-id-commonlanguage_ecapa/example-it.wav')
print(text_lab)

# French Example
out_prob, score, index, text_lab = classifier.classify_file('speechbrain/lang-id-commonlanguage_ecapa/example-fr.wav')
print(text_lab)
```

### [Spoken Language Understanding](https://huggingface.co/speechbrain/slu-timers-and-such-direct-librispeech-asr)

```python
from speechbrain.pretrained import EndToEndSLU
slu = EndToEndSLU.from_hparams("speechbrain/slu-timers-and-such-direct-librispeech-asr")
slu.decode_file("speechbrain/slu-timers-and-such-direct-librispeech-asr/math.wav")

```

### [Speech Separation](https://huggingface.co/speechbrain/sepformer-whamr)

```python
from speechbrain.pretrained import SepformerSeparation as separator
import torchaudio

model = separator.from_hparams(source="speechbrain/sepformer-whamr", savedir='pretrained_models/sepformer-whamr')

# for custom file, change path
est_sources = model.separate_file(path='speechbrain/sepformer-wsj02mix/test_mixture.wav') 

torchaudio.save("source1hat.wav", est_sources[:, :, 0].detach().cpu(), 8000)
torchaudio.save("source2hat.wav", est_sources[:, :, 1].detach().cpu(), 8000)

```

### [Speech Enhancement](https://huggingface.co/speechbrain/sepformer-whamr-enhancement)

```python
import torch
import torchaudio
from speechbrain.pretrained import SpectralMaskEnhancement

enhance_model = SpectralMaskEnhancement.from_hparams(
    source="speechbrain/metricgan-plus-voicebank",
    savedir="pretrained_models/metricgan-plus-voicebank",
)

# Load and add fake batch dimension
noisy = enhance_model.load_audio(
    "speechbrain/metricgan-plus-voicebank/example.wav"
).unsqueeze(0)

# Add relative length tensor
enhanced = enhance_model.enhance_batch(noisy, lengths=torch.tensor([1.]))

# Saving enhanced signal on disk
torchaudio.save('enhanced.wav', enhanced.cpu(), 16000)

```