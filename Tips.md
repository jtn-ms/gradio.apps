
- Use float32 for CPU, float16 for GPU

```python
# gpu
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.to("cuda")

# cpu
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
```

### Ask you.com if you have any questions

- https://you.com/search?q=layernormkernelimpl+not+implemented+for+%27half%27+stable+diffusion&tbm=youchat&cfr=chatb&cid=c2_314078a2-2905-4e3c-8556-c42927e00cb4
