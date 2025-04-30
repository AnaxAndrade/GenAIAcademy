# Paper sobre Stable Diffusion

## Denoising Diffusion Probabilistic Model (UC Berkeley)
**Link:** https://arxiv.org/pdf/2006.11239
**Abstract:**
We present high quality image synthesis results using diffusion probabilistic models,
a class of latent variable models inspired by considerations from nonequilibrium
thermodynamics. Our best results are obtained by training on a weighted variational
bound designed according to a novel connection between diffusion probabilistic
models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a
generalization of autoregressive decoding. On the unconditional CIFAR10 dataset,
we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On
256x256 LSUN, we obtain sample quality similar to ProgressiveGAN. Our implementation is available at https://github.com/hojonathanho/diffusion.

## Diffusion Models Beat GANs on Image Synthesis (OepnAI)
**Link:** https://arxiv.org/pdf/2105.05233
We show that diffusion models can achieve image sample quality superior to the
current state-of-the-art generative models. We achieve this on unconditional image synthesis by finding a better architecture through a series of ablations. For
conditional image synthesis, we further improve sample quality with classifier guidance: a simple, compute-efficient method for trading off diversity for fidelity using
gradients from a classifier. We achieve an FID of 2.97 on ImageNet 128×128,
4.59 on ImageNet 256×256, and 7.72 on ImageNet 512×512, and we match
BigGAN-deep even with as few as 25 forward passes per sample, all while maintaining better coverage of the distribution. Finally, we find that classifier guidance
combines well with upsampling diffusion models, further improving FID to 3.94
on ImageNet 256×256 and 3.85 on ImageNet 512×512. We release our code at
https://github.com/openai/guided-diffusion.

## High-Resolution Image Synthesis with Latent Diffusion Models (Stable Diffusion)

**Link:** https://arxiv.org/abs/2112.10752
<br>
**Abstract:**
By decomposing the image formation process into a sequential application of denoising autoencoders, diffusion models (DMs) achieve state-of-the-art synthesis results on image data and beyond. Additionally, their formulation allows for a guiding mechanism to control the image generation process without retraining. However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due to sequential evaluations. To enable DM training on limited computational resources while retaining their quality and flexibility, we apply them in the latent space of powerful pretrained autoencoders. In contrast to previous work, training diffusion models on such a representation allows for the first time to reach a near-optimal point between complexity reduction and detail preservation, greatly boosting visual fidelity. By introducing cross-attention layers into the model architecture, we turn diffusion models into powerful and flexible generators for general conditioning inputs such as text or bounding boxes and high-resolution synthesis becomes possible in a convolutional manner. Our latent diffusion models (LDMs) achieve a new state of the art for image inpainting and highly competitive performance on various tasks, including unconditional image generation, semantic scene synthesis, and super-resolution, while significantly reducing computational requirements compared to pixel-based DMs.