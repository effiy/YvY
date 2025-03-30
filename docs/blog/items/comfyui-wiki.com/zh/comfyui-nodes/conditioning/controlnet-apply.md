# 原始URL: https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply

# 抓取时间: 2025-03-30 21:02:33

[Skip to content](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#reach-skip-nav)
We detected your browser language. Would you like to switch to English version?
Don't ask today
Keep CurrentSwitch Language
帮助构建更好的 ComfyUI 知识库 [成为赞助者](https://comfyui-wiki.com/zh/patrons)
[![logo](https://comfyui-wiki.com/logo.svg)ComfyUI Wiki](https://comfyui-wiki.com/zh)
安装指南UI界面ComfyUI节点ComfyUI教程资源[新闻](https://comfyui-wiki.com/zh/news)其他
`CTRL K`
中文
`CTRL K`
  * [安装指南](https://comfyui-wiki.com/zh/install)
    * [1. 安装 ComfyUI](https://comfyui-wiki.com/zh/install/install-comfyui)
      * [1.1 ComfyUI Desktop](https://comfyui-wiki.com/zh/install/install-comfyui/comfyui-desktop-installation-guide)
      * [1.2 Windows](https://comfyui-wiki.com/zh/install/install-comfyui/install-comfyui-on-windows)
      * [1.3 Mac](https://comfyui-wiki.com/zh/install/install-comfyui/install-comfyui-on-mac)
      * [1.4 Linux](https://comfyui-wiki.com/zh/install/install-comfyui/install-comfyui-on-linux)
      * [1.5 Run on Cloud](https://comfyui-wiki.com/zh/install/install-comfyui/run-comfyui-on-cloud)
      * [1.6 Install Git](https://comfyui-wiki.com/zh/install/install-comfyui/install-git)
      * [1.7 秋叶启动器指南](https://comfyui-wiki.com/zh/install/install-comfyui/aaaki-comfyui-launcher-user-guide)
      * [1.8 GPU 购买参考](https://comfyui-wiki.com/zh/install/install-comfyui/gpu-buying-guide)
    * [2. 安装自定义节点](https://comfyui-wiki.com/zh/install/install-custom-nodes)
    * [3. 安装模型](https://comfyui-wiki.com/zh/install/install-models)
      * [3.1 安装检查点](https://comfyui-wiki.com/zh/install/install-models/install-checkpoint)
      * [3.2 安装 ControlNet](https://comfyui-wiki.com/zh/install/install-models/install-controlnet)
      * [3.3 安装 Embeddings](https://comfyui-wiki.com/zh/install/install-models/install-embeddings)
      * [3.4 安装 Hypernetwork](https://comfyui-wiki.com/zh/install/install-models/install-hypernetwork)
      * [3.5 安装 LoRA](https://comfyui-wiki.com/zh/install/install-models/install-lora)
      * [3.6 安装 VAE](https://comfyui-wiki.com/zh/install/install-models/install-vae)
  * [界面及设置](https://comfyui-wiki.com/zh/interface)
    * [1. 界面指南](https://comfyui-wiki.com/zh/interface/basic)
    * [2. 节点操作指南](https://comfyui-wiki.com/zh/interface/node-options)
    * [3. 工作流](https://comfyui-wiki.com/zh/interface/workflow)
    * [4. 提示词](https://comfyui-wiki.com/zh/interface/prompt)
    * [5.1 设置菜单](https://comfyui-wiki.com/zh/interface/menu)
    * [5.2 Comfy](https://comfyui-wiki.com/zh/interface/comfy)
    * [5.3 画面](https://comfyui-wiki.com/zh/interface/lite-graph)
    * [5.4 外观](https://comfyui-wiki.com/zh/interface/appearance)
    * [5.5 遮罩编辑器](https://comfyui-wiki.com/zh/interface/maskeditor)
    * [5.6 快捷键](https://comfyui-wiki.com/zh/interface/shortcuts)
    * [5.7 扩展](https://comfyui-wiki.com/zh/interface/extension)
    * [5.8 服务器配置](https://comfyui-wiki.com/zh/interface/server-config)
    * [5.9 关于](https://comfyui-wiki.com/zh/interface/about)
    * [6. 文件结构](https://comfyui-wiki.com/zh/interface/files)
  * [系列教程](https://comfyui-wiki.com/zh/tutorial)
    * [ComfyUI 基础入门教程](https://comfyui-wiki.com/zh/tutorial/basic)
      * [1.启动服务](https://comfyui-wiki.com/zh/tutorial/basic/how-to-run-comfyui-serve)
      * [2.首次图片生成](https://comfyui-wiki.com/zh/tutorial/basic/creating-your-first-image-by-the-first-time)
      * [3.与WebUI共用模型设置](https://comfyui-wiki.com/zh/tutorial/basic/link-models-between-comfyui-and-a1111)
      * [4.如何升级ComfyUI](https://comfyui-wiki.com/zh/tutorial/basic/how-to-update-comfyui)
      * [5.安装不同类型的模型](https://comfyui-wiki.com/zh/tutorial/basic/how-to-install-different-type-of-models)
      * [6.提示词基础](https://comfyui-wiki.com/zh/tutorial/basic/stable-diffusion-prompt-basic)
      * [7.局部重绘](https://comfyui-wiki.com/zh/tutorial/basic/how-to-inpaint-an-image-in-comfyui)
      * [8.扩图](https://comfyui-wiki.com/zh/tutorial/basic/how-to-outpaint-an-image-in-comfyui)
      * [9.图像放大](https://comfyui-wiki.com/zh/tutorial/basic/upscale-image)
      * [10. Embedding](https://comfyui-wiki.com/zh/tutorial/basic/embedding)
      * [11. LoRA](https://comfyui-wiki.com/zh/tutorial/basic/lora)
    * [ComfyUI 进阶教程](https://comfyui-wiki.com/zh/tutorial/advanced)
      * [1. Controlnet 教程](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-install-and-use-controlnet-models-in-comfyui)
      * [1.1 SD1.5 Canny ControlNet](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5)
      * [1.2 SD1.5 Depth ControlNet](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5)
      * [1.3 SD1.5 OpenPose ControlNet](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-openpose-controlnet-with-sd1.5)
      * [1.4 SD1.5 多ControlNet组合使用](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui)
      * [2.1 FLUX.1 文生图教程](https://comfyui-wiki.com/zh/tutorial/advanced/flux1-comfyui-guide-workflow-and-examples)
      * [2.2 FLUX.1 图生图教程](https://comfyui-wiki.com/zh/tutorial/advanced/flux1-comfyui-image-to-image-workflow-example)
      * [2.3 FLUX.1 Fill](https://comfyui-wiki.com/zh/tutorial/advanced/flux-fill-workflow-step-by-step-guide)
      * [2.4 FLUX.1 Redux](https://comfyui-wiki.com/zh/tutorial/advanced/flux-redux-workflow-step-by-step-guide)
      * [2.5 FLUX.1 ControlNet](https://comfyui-wiki.com/zh/tutorial/advanced/flux-controlnet-workflow-guide)
      * [3. SD 3.5 文生图教程](https://comfyui-wiki.com/zh/tutorial/advanced/stable-diffusion-3-5-comfyui-workflow)
      * [4. LTX 视频生成教程](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide)
      * [5.1. 腾讯混元 文生视频](https://comfyui-wiki.com/zh/tutorial/advanced/hunyuan-text-to-video-workflow-guide-and-example)
      * [5.2. 腾讯混元 图生视频](https://comfyui-wiki.com/zh/tutorial/advanced/hunyuan-image-to-video-workflow-guide-and-example)
      * [6. IC Light V2](https://comfyui-wiki.com/zh/tutorial/advanced/ic-light-v2)
      * [7. DeepSeek Janus Pro](https://comfyui-wiki.com/zh/tutorial/advanced/deepseek-janus-pro-workflow)
      * [8. Lumina Image 2](https://comfyui-wiki.com/zh/tutorial/advanced/lumina-image-2)
      * [9. Sonic Video](https://comfyui-wiki.com/zh/tutorial/advanced/sonic-video)
      * [10. Wan2.1](https://comfyui-wiki.com/zh/tutorial/advanced/wan21-video-model)
      * 3d
        * [Hunyuan3D 2.0](https://comfyui-wiki.com/zh/tutorial/advanced/3d/huanyuan3d-2)
    * [ComfyUI 专家教程](https://comfyui-wiki.com/zh/tutorial/expert)
  * [节点详解](https://comfyui-wiki.com/zh/comfyui-nodes)
    * Advanced
      * conditioning
        * [CLIP文本编码SDXL-ComfyUI节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/conditioning/clip-text-encode-sdxl)
        * [CLIP文本编码SDXL（Refiner）-ComfyUI节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/conditioning/clip-text-encode-sdxl-refiner)
        * [CLIP Text Encode Hunyuan DiT CLIP文本编码混元](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/conditioning/clip_text_encode_hunyuan_dit)
        * [设置条件时间-ComfyUI节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/conditioning/conditioning-settimestep-range)
        * [Conditioning Zero Out](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/conditioning/conditioning-zero-out)
        * flux
          * [CLIPTextEncodeFlux - ComfyUI节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/conditioning/flux/clip-text-encode-flux)
          * [FluxGuidance - ComfyUI 节点功能说明](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/conditioning/flux/flux-guidance)
      * loaders
        * [CLIP Loader](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/loaders/clip-loader)
        * [Load Checkpoint With Config (DEPRECATED)](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/loaders/deprecated-checkpoint-loader)
        * [Diffuser Loader｜扩散加载器-ComfyUI节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/loaders/deprecated-diffusers-loader)
        * [双CLIP加载器-ComfyUI节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/loaders/dual-clip-loader)
        * [UNET Loader | UNET加载器-ComfyUI节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/loaders/unet-loader)
      * model
        * [模型连续采样算法EDM](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/model/model-sampling-continuous-edm)
        * [模型离散采样算法](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/model/model-sampling-discrete)
        * [缩放CFG](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/model/rescale-cfg)
      * model-merging
        * [CheckpointSave 节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/model-merging/checkpoint-save)
        * [融合CLIP节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/model-merging/clip-merge-simple)
        * [保存CLIP节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/model-merging/clip-save)
        * [融合模型（相加）节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/model-merging/model-merge-add)
        * [融合模型（分层）节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/model-merging/model-merge-blocks)
        * [融合模型节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/model-merging/model-merge-simple)
        * [融合模型（相减）节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/model-merging/model-merge-subtract)
        * [保存VAE节点](https://comfyui-wiki.com/zh/comfyui-nodes/advanced/model-merging/vae-save)
    * Conditioning
      * 3d-models
        * [SZ123条件节点](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/3d-models/stablezero123-conditioning)
        * [SZ123条件(批次)节点](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/3d-models/stablezero123-conditioning-batched)
      * [CLIP设置停止层节点](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/clip-set-last-layer)
      * [CLIP文本编码器](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/clip-text-encode)
      * [CLIP视觉编码](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/clip-vision-encode)
      * [条件平均](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/conditioning-average)
      * [Conditioning(Combine) - 条件合并节点](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/conditioning-combine)
      * [Conditioning (Concat) - 条件联结节点](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/conditioning-concat)
      * [Conditioning (Set Area) - 条件采样区域](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/conditioning-set-area)
      * [Conditioning (Set Area with Percentage) - 按系数设置条件采样区域](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/conditioning-set-area-percentage)
      * [Conditioning (Set Area Strength) - 条件设置区域强度](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/conditioning-set-area-strength)
      * [Conditioning (Set Mask) - 条件设置遮罩](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/conditioning-set-mask)
      * [Apply ControlNet - 应用ControlNet节点](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply)
      * [Apply ControlNet (Advanced) - ControlNet高级应用](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply-advanced)
      * gligen
        * [GLIGEN文本框应用节点](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/gligen/gligen-text-box-apply)
      * inpaint
        * [内补模型条件节点](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/inpaint/inpaint-model-conditioning)
      * style-model
        * [风格模型应用节点](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/style-model/style-model-apply)
      * [unCLIP Conditioning - unCLIP条件](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/unclip-conditioning)
      * upscale-diffusion
        * [SD4X放大条件节点](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/upscale-diffusion/sd-4xupscale-conditioning)
      * video-models
        * [SVD_图像到视频_条件节点](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/video-models/svd-img2vid-conditioning)
    * Image
      * animation
        * [Save Animated PNG - 保存APNG](https://comfyui-wiki.com/zh/comfyui-nodes/image/animation/save-animated-png)
        * [Save Animated WEBP - 保存WEBP](https://comfyui-wiki.com/zh/comfyui-nodes/image/animation/save-animated-webp)
      * batch
        * [Image From Batch - 从批次获取图像](https://comfyui-wiki.com/zh/comfyui-nodes/image/batch/image-from-batch)
        * [Rebatch Images - 重设图像批次](https://comfyui-wiki.com/zh/comfyui-nodes/image/batch/rebatch-images)
        * [Repeat Image Batch](https://comfyui-wiki.com/zh/comfyui-nodes/image/batch/repeat-image-batch)
      * [Empty Image 空图像](https://comfyui-wiki.com/zh/comfyui-nodes/image/empty-image)
      * [Image Batch 图像组合批次](https://comfyui-wiki.com/zh/comfyui-nodes/image/image-batch)
      * [Image Composite Masked 图像遮罩复合](https://comfyui-wiki.com/zh/comfyui-nodes/image/image-composite-masked)
      * [Invert Image 图像反转](https://comfyui-wiki.com/zh/comfyui-nodes/image/image-invert)
      * [Image Pad For Outpainting 外补画板](https://comfyui-wiki.com/zh/comfyui-nodes/image/image-pad-for-outpaint)
      * [Load Image 加载图像](https://comfyui-wiki.com/zh/comfyui-nodes/image/load-image)
      * postprocessing
        * [Image Blend](https://comfyui-wiki.com/zh/comfyui-nodes/image/postprocessing/image-blend)
        * [Image Blur](https://comfyui-wiki.com/zh/comfyui-nodes/image/postprocessing/image-blur)
        * [Image Quantize](https://comfyui-wiki.com/zh/comfyui-nodes/image/postprocessing/image-quantize)
        * [Image Sharpen 图像锐化](https://comfyui-wiki.com/zh/comfyui-nodes/image/postprocessing/image-sharpen)
      * preprocessors
        * [Canny 节点](https://comfyui-wiki.com/zh/comfyui-nodes/image/preprocessors/canny)
      * [Preview Image 预览图像](https://comfyui-wiki.com/zh/comfyui-nodes/image/preview-image)
      * [Save Image 保存图像节点，ComfyUI 中保存图像到本地的方法](https://comfyui-wiki.com/zh/comfyui-nodes/image/save-image)
      * transform
        * [Image Crop 图像裁剪](https://comfyui-wiki.com/zh/comfyui-nodes/image/transform/image-crop)
      * upscaling
        * [Image Scale 图像缩放](https://comfyui-wiki.com/zh/comfyui-nodes/image/upscaling/image-scale)
        * [Image Scale By 图像按系数缩放节点](https://comfyui-wiki.com/zh/comfyui-nodes/image/upscaling/image-scale-by)
        * [Image Scale To Total Pixels 图像按像素缩放](https://comfyui-wiki.com/zh/comfyui-nodes/image/upscaling/image-scale-to-total-pixels)
        * [Image Upscale With Model 图像通过模型放大](https://comfyui-wiki.com/zh/comfyui-nodes/image/upscaling/image-upscale-with-model)
    * Latent
      * [Latent Upscale](https://comfyui-wiki.com/zh/comfyui-nodes/latent/latent-upscale)
      * [Empty Latent Image](https://comfyui-wiki.com/zh/comfyui-nodes/latent/empty-latent-image)
      * [Latent Upscale By](https://comfyui-wiki.com/zh/comfyui-nodes/latent/latent-upscale-by)
      * [Latent Composite](https://comfyui-wiki.com/zh/comfyui-nodes/latent/latent-composite)
      * [VAE Decode](https://comfyui-wiki.com/zh/comfyui-nodes/latent/vae-decode)
      * [VAE Encode](https://comfyui-wiki.com/zh/comfyui-nodes/latent/vae-encode)
      * [Latent Composite Masked](https://comfyui-wiki.com/zh/comfyui-nodes/latent/latent-composite-masked)
      * advanced
        * [Latent Add 潜变量相加](https://comfyui-wiki.com/zh/comfyui-nodes/latent/advanced/latent-add)
        * [Latent Batch Seed Behavior 潜变量批次随机种操作](https://comfyui-wiki.com/zh/comfyui-nodes/latent/advanced/latent-batch-seed-behavior)
        * [Latent Interpolate 潜变量插值](https://comfyui-wiki.com/zh/comfyui-nodes/latent/advanced/latent-interpolate)
        * [Latent Multiply 潜变量相乘](https://comfyui-wiki.com/zh/comfyui-nodes/latent/advanced/latent-multiply)
        * [Latent Subtract 潜变量相减](https://comfyui-wiki.com/zh/comfyui-nodes/latent/advanced/latent-subtract)
      * batch
        * [Latent Batch 潜变量批次](https://comfyui-wiki.com/zh/comfyui-nodes/latent/batch/latent-batch)
        * [Latent From Batch 从批次获取潜变量](https://comfyui-wiki.com/zh/comfyui-nodes/latent/batch/latent-from-batch)
        * [Rebatch Latents 重设Latent批次](https://comfyui-wiki.com/zh/comfyui-nodes/latent/batch/rebatch-latents)
        * [Repeat Latent Batch 复制Latent批次](https://comfyui-wiki.com/zh/comfyui-nodes/latent/batch/repeat-latent-batch)
      * inpaint
        * [Set Latent Noise Mask 设置Latent噪波遮罩](https://comfyui-wiki.com/zh/comfyui-nodes/latent/inpaint/set-latent-noise-mask)
        * [VAE Encode (for Inpainting) 编码用于内补的VAE](https://comfyui-wiki.com/zh/comfyui-nodes/latent/inpaint/vae-encode-for-inpaint)
      * transform
        * [Crop Latent 裁剪Latent](https://comfyui-wiki.com/zh/comfyui-nodes/latent/transform/latent-crop)
        * [Flip Latent 翻转Latent](https://comfyui-wiki.com/zh/comfyui-nodes/latent/transform/latent-flip)
        * [Rotate Latent](https://comfyui-wiki.com/zh/comfyui-nodes/latent/transform/latent-rotate)
      * video
        * [Empty Hunyuan Latent Video 空Latent视频（混元）节点教程](https://comfyui-wiki.com/zh/comfyui-nodes/latent/video/empty-hunyuan-latent-video)
    * Loaders
      * [Checkpoint Loader (Simple)](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/checkpoint-loader-simple)
      * [CLIP Vision Loader](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/clip-vision-loader)
      * [ControlNet Loader](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/controlnet-loader)
      * [Diff ControlNet Loader](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/diff-controlnet-loader)
      * [GLIGEN Loader](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/gligen-loader)
      * [Hypernetwork Loader](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/hypernetwork-loader)
      * [Lora Loader - ComfyUI 节点说明](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/lora-loader)
      * [Lora Loader Model Only](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/lora-loader-model-only)
      * [Style Model Loader](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/style-model-loader)
      * [unCLIP Checkpoint Loader](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/unclip-checkpoint-loader)
      * [Upscale Model Loader](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/upscale-model-loader)
      * [VAE Loader](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/vae-loader)
      * video-models
        * [Image Only Checkpoint Loader (img2vid model)](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/video-models/image-only-checkpoint-loader)
    * Mask
      * compositing
        * [Join Image with Alpha](https://comfyui-wiki.com/zh/comfyui-nodes/mask/compositing/join-image-with-alpha)
        * [Porter-Duff Image Composite](https://comfyui-wiki.com/zh/comfyui-nodes/mask/compositing/porter-duff-image-composite)
        * [Split Image with Alpha](https://comfyui-wiki.com/zh/comfyui-nodes/mask/compositing/split-image-with-alpha)
      * [Crop Mask](https://comfyui-wiki.com/zh/comfyui-nodes/mask/crop-mask)
      * [Feather Mask](https://comfyui-wiki.com/zh/comfyui-nodes/mask/feather-mask)
      * [Grow Mask](https://comfyui-wiki.com/zh/comfyui-nodes/mask/grow-mask)
      * [Image Color To Mask](https://comfyui-wiki.com/zh/comfyui-nodes/mask/image-color-to-mask)
      * [Image To Mask](https://comfyui-wiki.com/zh/comfyui-nodes/mask/image-to-mask)
      * [Invert Mask](https://comfyui-wiki.com/zh/comfyui-nodes/mask/invert-mask)
      * [Load Image (as Mask)](https://comfyui-wiki.com/zh/comfyui-nodes/mask/load-image-mask)
      * [Mask Composite](https://comfyui-wiki.com/zh/comfyui-nodes/mask/mask-composite)
      * [Mask To Image](https://comfyui-wiki.com/zh/comfyui-nodes/mask/mask-to-image)
      * [Solid Mask 纯色遮罩](https://comfyui-wiki.com/zh/comfyui-nodes/mask/solid-mask)
    * Sampling
      * custom-sampling
        * [SamplerCustom](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/custom-sampling/sampler-custom)
        * samplers
          * [KSampler Select](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/custom-sampling/samplers/k-sampler-select)
          * [Sampler DPMPP_2M_SDE](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/custom-sampling/samplers/sampler-dpmpp-2m-sde)
          * [Sampler DPMPP_SDE](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/custom-sampling/samplers/sampler-dpmpp-sde)
        * schedulers
          * [Basic Scheduler](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/custom-sampling/schedulers/basic-scheduler)
          * [Exponential Scheduler](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/custom-sampling/schedulers/exponential-scheduler)
          * [Karras Scheduler](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/custom-sampling/schedulers/karras-scheduler)
          * [Polyexponential Scheduler](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/custom-sampling/schedulers/polyexponential-scheduler)
          * [SD Turbo Scheduler](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/custom-sampling/schedulers/sd-turbo-scheduler)
          * [VP Scheduler](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/custom-sampling/schedulers/vp-scheduler)
        * sigmas
          * [Flip Sigmas](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/custom-sampling/sigmas/flip-sigmas)
          * [Split Sigmas](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/custom-sampling/sigmas/split-sigmas)
      * [KSampler](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/k-sampler)
      * [KSampler (Advanced)](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/k-sampler-advanced)
      * [Sampler 采样器详解](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/sampler)
      * video-models
        * [Video Linear CFG Guidance](https://comfyui-wiki.com/zh/comfyui-nodes/sampling/video-models/video-linear-cfg-guidance)
    * Utils
      * [Note 注释节点](https://comfyui-wiki.com/zh/comfyui-nodes/utils/note)
      * [Primitive 元节点](https://comfyui-wiki.com/zh/comfyui-nodes/utils/primitive)
      * [Reroute 转接点](https://comfyui-wiki.com/zh/comfyui-nodes/utils/reroute)
      * [Terminal Log (Manager)](https://comfyui-wiki.com/zh/comfyui-nodes/utils/terminal-log)
  * [ComfyUI 官方示例](https://comfyui-wiki.com/zh/workflows)
    * [1. 图生图工作流](https://comfyui-wiki.com/zh/workflows/img2img)
    * [2. 两步文生图工作流](https://comfyui-wiki.com/zh/workflows/2-pass-txt2img)
    * [3. 局部重绘工作流](https://comfyui-wiki.com/zh/workflows/inpaint)
    * [4. 区域合成工作流](https://comfyui-wiki.com/zh/workflows/area-composition)
    * [5. 超分辨率模型工作流](https://comfyui-wiki.com/zh/workflows/upscale-models)
    * [6. LoRA 模型工作流](https://comfyui-wiki.com/zh/workflows/lora)
    * [7. ControlNet 工作流](https://comfyui-wiki.com/zh/workflows/controlnet)
    * [8. 噪声潜空间合成工作流](https://comfyui-wiki.com/zh/workflows/noisy-latent-composition)
    * [9. 文本反转嵌入工作流](https://comfyui-wiki.com/zh/workflows/textual-inversion-embeddings)
    * [10. 模型编辑工作流](https://comfyui-wiki.com/zh/workflows/edit-models)
    * [11. 模型合并工作流](https://comfyui-wiki.com/zh/workflows/model-merging)
    * [12. SDXL 工作流](https://comfyui-wiki.com/zh/workflows/sdxl)
    * [13. Stable Cascade 工作流](https://comfyui-wiki.com/zh/workflows/stable-cascade)
    * [14. UnCLIP 工作流](https://comfyui-wiki.com/zh/workflows/unclip)
    * [15. Hypernetworks 工作流](https://comfyui-wiki.com/zh/workflows/hypernetworks)
    * [16. Gligen 工作流](https://comfyui-wiki.com/zh/workflows/gligen)
    * [17. 3D 示例工作流](https://comfyui-wiki.com/zh/workflows/3d)
    * [18. 视频生成工作流](https://comfyui-wiki.com/zh/workflows/video)
    * [LCM 示例](https://comfyui-wiki.com/zh/workflows/lcm)
    * [ComfyUI SDXL Turbo 示例](https://comfyui-wiki.com/zh/workflows/sdturbo)
  * [相关资源](https://comfyui-wiki.com/zh/resource)
    * [Stable Diffusion](https://comfyui-wiki.com/zh/resource/stable-diffusion-models)
    * [Flux](https://comfyui-wiki.com/zh/resource/flux)
    * [LoRA](https://comfyui-wiki.com/zh/resource/lora-models)
    * [ControlNet](https://comfyui-wiki.com/zh/resource/controlnet-models)
      * [Flux](https://comfyui-wiki.com/zh/resource/controlnet-models/controlnet-flux-1)
      * [SDXL](https://comfyui-wiki.com/zh/resource/controlnet-models/controlnet-sdxl)
      * [v1.1 for SD1.5/SD2](https://comfyui-wiki.com/zh/resource/controlnet-models/controlnet-v1-1-sd15-sd2)
      * [V1 for SD1.5](https://comfyui-wiki.com/zh/resource/controlnet-models/controlnet-v1-sd15)
    * [Custom Nodes](https://comfyui-wiki.com/zh/resource/custom-nodes)
    * [Embedding](https://comfyui-wiki.com/zh/resource/embedding-models)
    * [Upscale Models](https://comfyui-wiki.com/zh/resource/upscale-models)
    * [VAE](https://comfyui-wiki.com/zh/resource/vae-models)
    * [Unet](https://comfyui-wiki.com/zh/resource/unet-models)
    * [ComfyUI官方资源](https://comfyui-wiki.com/zh/resource/comfyui-official-resources)
    * [ComfyUI 相关工具与资源](https://comfyui-wiki.com/zh/resource/others)
    * [Tencent-Hunyuan 腾讯混元相关资源](https://comfyui-wiki.com/zh/resource/tencent-hunyuan)
  * [常见问题](https://comfyui-wiki.com/zh/faq)
    * [ComfyUI Fast Groups 替代方案和使用指南](https://comfyui-wiki.com/zh/faq/comfyui-fast-groups-alternatives)
    * [解决ComfyUI Manager安全级别报错「This action is not allowed」的完整指南](https://comfyui-wiki.com/zh/faq/fix-comfyui-manager-security-level-error)
    * [如何在局域网中访问 ComfyUI](https://comfyui-wiki.com/zh/faq/how-to-access-comfyui-on-lan)
    * [如何在 ComfyUI 中调整字体大小：分步指南](https://comfyui-wiki.com/zh/faq/how-to-change-font-size)
    * [如何更改 ComfyUI 的输出文件夹位置](https://comfyui-wiki.com/zh/faq/how-to-change-output-folder)
    * [如何启用 ComfyUI 新版本菜单](https://comfyui-wiki.com/zh/faq/how-to-enable-new-menu)
    * [为什么使用相同的种子值，ComfyUI 和 A1111 生成的图像不一样？](https://comfyui-wiki.com/zh/faq/why-different-images-from-a1111)


中文
System
#### Sponsors
[![RunComfy](https://comfyui-wiki.com/patron/runcomfy-logo.png)RunComfyComfyUI Cloud](https://www.runcomfy.com)[![Comfy Deploy](https://comfyui-wiki.com/patron/comfydeploy-logo.png)Comfy DeployRun and deploy your ComfyUI workflows](https://comfydeploy.com/?utm_source='comfyui-wiki'&utm_content='sidebar')[![Comfy Online](https://comfyui-wiki.com/patron/comfyonline-logo.png)Comfy OnlineRun ComfyUI workflows online and deploy APIs with one click](https://www.comfyonline.app/)[![Comfy.ICU](https://comfyui-wiki.com/patron/comfy-icu-logo.png)Comfy.ICURun ComfyUI in the cloud](https://comfy.icu/)[![InstaSD](https://comfyui-wiki.com/patron/instasd-logo.png)InstaSDHow creative teams run & deploy workflows](https://www.instasd.com/)
  * [Apply ControlNet 文档说明](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-文档说明)
  * [Apply ControlNet 输入类型](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-输入类型)
  * [Apply ControlNet 输出类型](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-输出类型)
  * [ComfyUI ControlNet 使用示例](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#comfyui-controlnet-使用示例)
  * [ControlNet 阶段控制设置说明](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#controlnet-阶段控制设置说明)
  * [1. 各类型ControlNet阶段控制参数配置参考](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#1-各类型controlnet阶段控制参数配置参考)
  * [2. 经典场景配置模板](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#2-经典场景配置模板)
  * [2.1、建筑可视化设计](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#21建筑可视化设计)
  * [2.2、游戏角色设计](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#22游戏角色设计)
  * [2.3、产品概念设计](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#23产品概念设计)
  * [2.4、医学可视化](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#24医学可视化)
  * [2.5、电影场景合成](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#25电影场景合成)
  * [2.6、电商广告设计](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#26电商广告设计)
  * [3. 专家级调整策略](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#3-专家级调整策略)
  * [3.1 阶段权重衰减模型](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#31-阶段权重衰减模型)
  * [3.2 多ControlNet冲突解决方案](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#32-多controlnet冲突解决方案)
  * [4. 常见问题速查](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#4-常见问题速查)
  * [相关资源](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#相关资源)
  * [Apply ControlNet (OLD) 旧版本节点说明](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-old-旧版本节点说明)
  * [Apply ControlNet (OLD) 输入类型](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-old-输入类型)
  * [Apply ControlNet (OLD) 输出类型](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-old-输出类型)


[](https://forms.gle/LRjjgeMwDYLdwXbk9)
[节点详解](https://comfyui-wiki.com/zh/comfyui-nodes "节点详解")[Conditioning](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/3d-models "Conditioning")Apply ControlNet - 应用ControlNet节点
←→
[新闻|字节跳动发布 InfiniteYou：保留用户身份特征的灵活图像再创作框架2025/03/21](https://comfyui-wiki.com/zh/news/2025-03-21-bytedance-infiniteyou)
# Apply ControlNet 应用ControlNet节点
💡
目前文档是原来 `Apply ControlNet(Advanced)`节点的说明，最早的 `Apply ControlNet` 节点已被重命名为 `Apply ControlNet(Old)`，但 comfyui.org 为了保证兼容性，在你下载到的许多工作流文件夹里应该还可以看到 `Apply ControlNet(Old)` 节点，但是目前你已经无法通过搜索或者节点列表看到 `Apply ControlNet(Old)` 节点，所以请使用 `Apply ControlNet` 节点。
![Apply ControlNet](https://comfyui-wiki.com/_next/static/media/apply-controlnet.e906d535.jpg)
此节点将 ControlNet 应用于给定的图像和条件，根据控制网络的参数和指定的强度调整图像的属性，比如 Depth、OpenPose、Canny、HED等等。
## Apply ControlNet 文档说明[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-文档说明)
  * 类名：`ControlNet应用`
  * 类别：`条件`
  * 输出节点：`False`


使用 controlNet 要求对输入图像进行预处理，由于ComfyUI 初始节点不带处理器和 controlNet 模型，所以请先安装ContrlNet预处理器[这里下载与处理器](https://github.com/Fannovel16/comfy_controlnet_preprocessors)和contrlNet 对应的模型。
## Apply ControlNet 输入类型[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-输入类型)
参数名称| 数据类型| 作用  
---|---|---  
`positive`| `CONDITIONING`| 正向条件数据，来自[CLIP文本编码器](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/clip-text-encode)或者其它条件输入  
`negative`| `CONDITIONING`| 负向条件数据，来自[CLIP文本编码器](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/clip-text-encode)或者其它条件输入  
`control_net`| `CONTROL_NET`| 要应用的controlNet模型，通常输入来自 [controlNt加载器](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/controlnet-loader)  
`image`| `IMAGE`| 用于 controlNet 应用的图片，需要经过预处理器处理  
`vae`| `VAE`| Vae模型输入  
`strength`| `FLOAT`| 用来控制网络调整的强度，取值0～10。建议取值在0.5～1.5之间比较合理，越小则模型会发挥越高的自由度，越大则会被限制得越严格,过高会出现很诡异的画面。你也可以通过自己测试来调整这个值，用来微调控制网络对图像产生的影响。  
`start_percent`| `FLOAT`| 取值 0.000～1.000，确定开始应用controlNet的百分比，比如取值0.2，意味着ControlNet的引导将在扩散过程完成20%时开始影响图像生成  
`end_percent`| `FLOAT`| 取值 0.000～1.000，确定结束应用controlNet的百分比，比如取值0.8，意味着ControlNet的引导将在扩散过程完成80%时停止影响图像生成  
## Apply ControlNet 输出类型[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-输出类型)
参数名称| 数据类型| 作用  
---|---|---  
`positive`| `CONDITIONING`| 经过ControlNet 处理后的正向条件数据，可以输出到下一个ControlNet 或者 K采样器等节点  
`negative`| `CONDITIONING`| 经过ControlNet 处理后的负向条件数据，可以输出到下一个ControlNet 或者 K采样器等节点  
💡
如果要使用**T2IAdaptor样式模型** ，请改用`Apply Style Model`节点
## ComfyUI ControlNet 使用示例[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#comfyui-controlnet-使用示例)
访问下面的页面查看示例
  * [ComfyUI OpenPose controlNet使用示例](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-openpose-controlnet-with-sd1.5)
  * [ComfyUI Depth controlNet使用示例](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5)
  * [ComfyUI Canny controlNet使用示例](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5)
  * [ComfyUI Multi ControlNet使用示例](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui)


## ControlNet 阶段控制设置说明[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#controlnet-阶段控制设置说明)
在节点的设置中你可以看到有 `start_percent`和 `end_percent`两个参数，这两个参数可以用来控制 ControlNet 在生成过程中的应用阶段，在使用 ControlNet 时
  * 你可以先设置`start_percent`和 `end_percent`为默认的 0.000 和 1.000，然后根据需要调整这两个参数的值，来查看应用的效果


下面是对于阶段控制的一些图例说明
### 1. 各类型ControlNet阶段控制参数配置参考[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#1-各类型controlnet阶段控制参数配置参考)
类型| 推荐权重| 阶段范围| 关键预处理参数| 最佳应用场景| 特别技巧  
---|---|---|---|---|---  
**Canny**|  0.8-1.2| 0.0-0.4| 阈值:100/200, 锐化15%| 建筑/产品设计| 透明材质开启Invert，复杂结构分段处理  
**HED**|  0.6-0.9| 0.2-0.7| 高斯模糊σ=1.5, 平滑20%| 人像/服装设计| Anime模式适合二次元，Realism模式保留真实细节  
**MLSD**|  0.7-1.0| 0.3-0.8| 最小线长15px, 角度容差15度| 工程制图| 墙面倾斜时权重+0.2，玻璃幕墙降权0.3  
**Depth**|  0.7-1.0| 0.2-0.9| MiDaS大模型, 3D映射| VR/医学可视化| 近景增强模式提升主体细节，ZoeDepth适合微距场景  
**Normal**|  0.5-0.8| 0.4-1.0| 分辨率2048px, 环境光遮蔽0.3| 产品渲染| 金属材质开启Specular，多光源合成增强立体感  
**Scribble**|  0.4-0.7| 0.5-1.0| SoftEdge模糊3px, 色相容差15%| 概念设计| 渐变区域使用50%透明度蒙版，Pantone色库保持品牌一致性  
**Lineart**|  0.6-0.9| 0.3-1.0| 抗锯齿开启, 线宽±2px| 角色原画| Anime模式线稿简化，Realism模式保留复杂褶皱  
**OpenPose**|  0.9-1.1| 0.0-0.3| 25点骨骼, 手部细节增强| 动态捕捉| 运动模糊补偿防止残影，武术动作提升权重至1.2  
**Segmentation**|  0.8-1.0| 0.0-0.7| ADEPT 2.0, 蒙版羽化10px| 广告合成| 天空区域降权0.2，建筑边缘锐化+20%  
**Tile**|  0.3-0.6| 0.4-0.9| 256x256分块, 重复率30%| 材质生成| Variation随机化增加自然感，砖墙纹理开启无缝拼接  
### 2. 经典场景配置模板[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#2-经典场景配置模板)
#### 2.1、建筑可视化设计[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#21建筑可视化设计)
控制类型| 权重| 阶段范围| 预处理参数| 调整技巧  
---|---|---|---|---  
Canny| 1.0| 0.0-0.4| 阈值100/200| 玻璃幕墙开启Invert  
Depth| 0.8| 0.2-0.7| MiDaS大模型| 中景区域增强20%  
MLSD| 0.6| 0.5-0.9| 最小线长20px| 倾斜墙体权重提升至0.8  
#### 2.2、游戏角色设计[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#22游戏角色设计)
控制类型| 权重| 阶段范围| 预处理参数| 动态调节  
---|---|---|---|---  
OpenPose| 1.0| 0.0-0.3| 完整骨骼| 第20步后降权至0.7  
Lineart| 0.7| 0.4-1.0| Anime模式| 装备区域权重+0.1  
Scribble| 0.5| 0.5-1.0| SoftEdge模糊2px| 色块边界强度设为0.3  
#### 2.3、产品概念设计[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#23产品概念设计)
控制类型| 权重| 阶段范围| 预处理参数| 材质优化  
---|---|---|---|---  
HED| 0.9| 0.0-0.3| 高斯模糊σ=1.5| 金属表面开启Specular  
Normal| 0.7| 0.2-0.6| 分辨率2048x2048| 塑料材质降权至0.5  
Depth| 0.6| 0.5-0.9| 近景增强| 背景虚化强度1.2  
#### 2.4、医学可视化[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#24医学可视化)
控制类型| 权重| 阶段范围| 预处理参数| 精度控制  
---|---|---|---|---  
Scribble| 0.8| 0.0-0.5| 红色标注线| 器官边界容差±2px  
Depth| 0.7| 0.4-0.8| CT扫描模式| 分层间距0.1mm  
Lineart| 0.9| 0.7-1.0| Ultra Detail| 血管路径精度1px  
#### 2.5、电影场景合成[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#25电影场景合成)
控制类型| 权重| 阶段范围| 预处理参数| 氛围营造  
---|---|---|---|---  
Seg| 0.9| 0.0-0.6| ADEPT模型| 天空区域降权0.2  
Shuffle| 0.6| 0.3-0.8| 色温5500K| 霓虹灯区权重0.8  
Depth| 0.7| 0.5-1.0| 动态范围压缩| 前景锐化强度1.5  
#### 2.6、电商广告设计[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#26电商广告设计)
控制类型| 权重| 阶段范围| 预处理参数| 商业优化  
---|---|---|---|---  
Canny| 1.2| 0.0-0.4| 边缘锐化+15%| 反光材质增强模式  
Scribble| 0.7| 0.3-0.7| Pantone色库| 品牌色容差±5%  
Inpaint| 0.5| 0.6-1.0| 羽化半径15px| 文字区域保护蒙版  
> **复制说明** ：完整选中从第一个`#`到本行内容，确保包含所有表格与流程图
### 3. 专家级调整策略[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#3-专家级调整策略)
#### 3.1 阶段权重衰减模型[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#31-阶段权重衰减模型)
生成进度| 控制类型| 衰减曲线| 公式示例  
---|---|---|---  
0-30%| 结构控制| 恒定强度| strength = 1.0  
30-70%| 空间控制| 线性衰减| strength = 1.0 - (step-30)/40*0.5  
70-100%| 细节控制| 逆向增强| strength = 0.5 + (step-70)/30*0.5  
#### 3.2 多ControlNet冲突解决方案[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#32-多controlnet冲突解决方案)
冲突类型| 可视化表现| 解决策略  
---|---|---  
结构-空间冲突| 物体漂浮/透视错误| 设置阶段间隔≥0.15  
空间-细节冲突| 材质扭曲/反光异常| 添加区域遮罩隔离控制范围  
结构-细节冲突| 关键特征丢失| 提升结构控制强度20%  
### 4. 常见问题速查[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#4-常见问题速查)
**Q1：控制效果突然消失？** ✅ 检查end_percent是否过早结束（建议≥0.8） ✅ 确认没有其他ControlNet覆盖该区域
**Q2：生成结果出现重影？** ✅ 降低阶段重叠度（建议≤20%） ✅ 为冲突ControlNet设置排除遮罩
**Q3：显存不足如何优化？** ✅ 采用阶梯式阶段配置（示例：0.0-0.3 → 0.4-0.6 → 0.7-1.0） ✅ 降低非关键ControlNet的分辨率至512px
## 相关资源[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#相关资源)
  * 模型资源：[controlNet模型资源下载](https://comfyui-wiki.com/zh/resource/controlnet-models)
  * 预处理器插件：[ComfyUI ControlNet Auxiliary Preprocessors](https://github.com/Fannovel16/comfyui_controlnet_aux)


## Apply ControlNet (OLD) 旧版本节点说明[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-old-旧版本节点说明)
![Apply ControlNet](https://comfyui-wiki.com/_next/static/media/Apply_ControlNet.b992918d.jpg) 这个节点为早期版本的 Apply ControlNet 节点，目前节点相关选项已更新，为了保证兼容性在 ComfyUI 中如果你下载了使用旧版本节点的工作流则会显示为此节点，你可以更换为新的 Apply ControlNet 节点。
### Apply ControlNet (OLD) 输入类型[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-old-输入类型)
参数名称| 数据类型| 作用  
---|---|---  
`条件`| `CONDITIONING`| 条件数据，来自[CLIP文本编码器](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/clip-text-encode)或者其它条件输入（如另一个条件节点的输入）  
`control_net`| `CONTROL_NET`| 要应用的controlNet模型，通常输入来自 [controlNt加载器](https://comfyui-wiki.com/zh/comfyui-nodes/loaders/controlnet-loader)  
`image`| `IMAGE`| 用于 controlNet 应用的图片，需要经过预处理器处理  
`强度`| `FLOAT`| 用来控制网络调整的强度，取值0～10。建议取值在0.5～1.5之间比较合理，越小则模型会发挥越高的自由度，越大则会被限制得越严格,过高会出现很诡异的画面。你也可以通过自己测试来调整这个值，用来微调控制网络对图像产生的影响。  
### Apply ControlNet (OLD) 输出类型[](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-old-输出类型)
参数名称| 数据类型| 作用  
---|---|---  
`条件`| `CONDITIONING`| 经过ControlNet 处理后的条件数据，可以输出到下一个ControlNet 或者 K采样器等节点  
Last updated on 2025年3月24日
[Conditioning (Set Mask) - 条件设置遮罩](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/conditioning-set-mask "Conditioning \(Set Mask\) - 条件设置遮罩")[Apply ControlNet (Advanced) - ControlNet高级应用](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply-advanced "Apply ControlNet \(Advanced\) - ControlNet高级应用")
中文
System
[![Logo](https://comfyui-wiki.com/logo.svg)ComfyUI-Wiki速查手册](https://comfyui-wiki.com/zh)
[](https://x.com/ComfyUIWiki)
![WeChat QR Code](https://comfyui-wiki.com/qrcode.jpg)
### 知识文档
  * [ComfyUI 安装教程](https://comfyui-wiki.com/zh/install)
  * [ComfyUI Node 节点速查手册](https://comfyui-wiki.com/zh/comfyui-nodes)
  * [ComfyUI 各类模型安装教程](https://comfyui-wiki.com/zh/install/install-models)
  * [ComfyUI 使用教程](https://comfyui-wiki.com/zh/tutorial)
  * [ComfyUI 工作流示例](https://comfyui-wiki.com/zh/workflows)


### 在线资源
  * [ComfyUI插件资源下载](https://comfyui-wiki.com/zh/resource/custom-nodes)
  * [Stable Diffusion LoRA 模型下载](https://comfyui-wiki.com/zh/resource/lora-models)
  * [Stable Diffusion Checkpoint 模型下载](https://comfyui-wiki.com/zh/resource/stable-diffusion-models)
  * [Stable Diffusion Embeddings 模型下载](https://comfyui-wiki.com/zh/resource/embedding-models)
  * [Stable Diffusion 放大模型下载](https://comfyui-wiki.com/zh/resource/upscale-models)
  * [Stable Diffusion VAE模型下载](https://comfyui-wiki.com/zh/resource/vae-models)
  * [Stable Diffusion ControlNet模型下载](https://comfyui-wiki.com/zh/resource/controlnet-models)


### 更多
  * [ComfyUI常见问题](https://comfyui-wiki.com/zh/faq)
  * [Stable Diffusion 常见术语表](https://comfyui-wiki.com/zh/glossary)
  * [服务条款](https://comfyui-wiki.com/zh/terms-of-service)
  * [隐私政策](https://comfyui-wiki.com/zh/privacy-policy)
  * [网站地图](https://comfyui-wiki.com/sitemap.xml)
  * [问题反馈](https://forms.gle/Mc7S1hNSWtdyZVzs8)


版权所有 © 2025 ComfyUI-Wiki. 保留所有权利。
