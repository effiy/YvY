# 原始URL: https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5

# 抓取时间: 2025-03-30 21:02:09

[Skip to content](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#reach-skip-nav)
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
  * [SD1.5 Canny ControlNet 简介](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#sd15-canny-controlnet-简介)
  * [Canny ControlNet 主要特点](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#canny-controlnet-主要特点)
  * [本篇教程准备工作](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#本篇教程准备工作)
  * [1. 更新 ComfyUI 并安装必要模型](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#1-更新-comfyui-并安装必要模型)
  * [2. 模型存放位置](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#2-模型存放位置)
  * [3. SD1.5 Canny ControlNet 工作流文件下载](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#3-sd15-canny-controlnet-工作流文件下载)
  * [工作流说明](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#工作流说明)
  * [关键节点说明](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#关键节点说明)
  * [使用步骤](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#使用步骤)
  * [使用技巧和建议](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#使用技巧和建议)
  * [实用示例](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#实用示例)
  * [相关资源](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#相关资源)


[](https://forms.gle/LRjjgeMwDYLdwXbk9)
[系列教程](https://comfyui-wiki.com/zh/tutorial "系列教程")[ComfyUI 进阶教程](https://comfyui-wiki.com/zh/tutorial/advanced "ComfyUI 进阶教程")1.1 SD1.5 Canny ControlNet
←→
[新闻|字节跳动发布 InfiniteYou：保留用户身份特征的灵活图像再创作框架2025/03/21](https://comfyui-wiki.com/zh/news/2025-03-21-bytedance-infiniteyou)
# ComfyUI 中如何使用 Canny ControlNet SD1.5 模型 - 完整指南
## SD1.5 Canny ControlNet 简介[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#sd15-canny-controlnet-简介)
![SD1.5 Canny ControlNet](https://comfyui-wiki.com/_next/static/media/canny-controlnet-sd1.5-compare.f2165a02.jpg) Canny ControlNet 是 ControlNet 模型中最常用的一种。它使用 Canny 边缘检测算法来提取图像中的边缘信息,然后利用这些边缘信息来引导 AI 生成图像。
这篇教程是关于 SD1.5 模型的 Canny ControlNet 模型的使用
其它相关内容： [ControlNet 模型安装使用教程汇总篇](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-install-and-use-controlnet-models-in-comfyui) [ControlNet 模型下载地址](https://comfyui-wiki.com/zh/resource/controlnet-models)
### Canny ControlNet 主要特点[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#canny-controlnet-主要特点)
  * **保持结构** : 能够很好地保持原始图像的基本结构和轮廓
  * **灵活性强** : 可以通过调整边缘检测的参数来控制引导的强度
  * **适用范围广** : 适合素描、线稿、建筑设计等多种场景
  * **效果稳定** : 相比其他 ControlNet 模型,Canny 的引导效果更加稳定和可预测


## 本篇教程准备工作[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#本篇教程准备工作)
### 1. 更新 ComfyUI 并安装必要模型[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#1-更新-comfyui-并安装必要模型)
由于部分节点使用的是新的 ComfyUI 节点，所以需要先更新 ComfyUI 到最新版本
  * 更新 ComfyUI 请参考 [ComfyUI 更新教程](https://comfyui-wiki.com/zh/tutorial/basic/how-to-update-comfyui)


首先需要安装以下模型:
模型类型| 模型文件| 下载地址  
---|---|---  
SD1.5 基础模型| dreamshaper_8.safetensors| [Civitai](https://civitai.com/models/4384/dreamshaper)  
Canny ControlNet 模型| control_v11p_sd15_canny.pth| [Hugging Face](https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11p_sd15_canny.pth)  
VAE 模型(可选)| vae-ft-mse-840000-ema-pruned.safetensors| [Hugging Face](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/blob/main/vae-ft-mse-840000-ema-pruned.safetensors)  
### 2. 模型存放位置[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#2-模型存放位置)
请按照以下结构放置模型文件:
```
📁ComfyUI
├── 📁models
│  ├── 📁checkpoints
│  │  └── 📁SD1.5
│  │    └── dreamshaper_8.safetensors
│  ├── 📁controlnet
│  │  └── 📁SD1.5
│  │    └── control_v11p_sd15_canny.pth
│  └── 📁vae
│    └── vae-ft-mse-840000-ema-pruned.safetensors
```

### 3. SD1.5 Canny ControlNet 工作流文件下载[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#3-sd15-canny-controlnet-工作流文件下载)
SD1.5 Canny ControlNet Workflow
保存下面的图像到本地，在载入工作流后在 LoadImage 节点中选择加载这张图片 ![SD1.5 Canny ControlNet Workflow](https://comfyui-wiki.com/_next/static/media/SD1.5-Controlnet-Canny-comfyui-wiki.52a4f479.png)
## 工作流说明[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#工作流说明)
这个工作流主要包含以下几个部分:
  1. **模型加载部分** : 加载 SD 模型、VAE 模型和 ControlNet 模型
  2. **提示词编码部分** : 处理正面和负面提示词
  3. **图像处理部分** : 包括图像加载和 Canny 边缘检测
  4. **ControlNet 控制部分** : 将边缘信息应用到生成过程
  5. **采样和保存部分** : 生成最终图像并保存


### 关键节点说明[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#关键节点说明)
  1. **LoadImage** : 用于加载输入图片
  2. **Canny** : 进行边缘检测,有两个重要参数:
     * low_threshold: 低阈值,控制边缘检测的敏感度
     * high_threshold: 高阈值,控制边缘的连续性
  3. **ControlNetLoader** : 加载 ControlNet 模型
  4. **ControlNetApplyAdvanced** : 控制 ControlNet 的应用方式,包含以下重要参数:
     * strength: 控制强度
     * start_percent: 开始影响的时间点
     * end_percent: 结束影响的时间点


## 使用步骤[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#使用步骤)
  1. **导入工作流**
     * 下载本篇教程的工作流文件
     * 在 ComfyUI 中点击 “Load”，或者直接将下载后的 JSON 文件拖入 ComfyUI 中
  2. **准备输入图片**
     * 准备一张你想要处理的图片
     * 使用 LoadImage 节点加载图片
  3. **调整 Canny 参数**
     * low_threshold 建议范围: 0.2-0.5
     * high_threshold 建议范围: 0.5-0.8
     * 可以通过 PreviewImage 节点实时预览边缘检测效果
  4. **设置生成参数**
     * 在 KSampler 节点中: 
       * steps: 建议 20-30
       * cfg: 建议 7-8
       * sampler_name: 推荐使用 “dpmpp_2m”
       * scheduler: 推荐使用 “karras”
  5. **调整 ControlNet 强度**
     * strength: 1.0 表示完全跟随边缘信息
     * 可以根据需要降低 strength 值来减弱控制


## 使用技巧和建议[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#使用技巧和建议)
  1. **边缘检测参数调整**
     * 如果边缘太多: 提高 threshold 值
     * 如果边缘太少: 降低 threshold 值
     * 建议先通过 PreviewImage 预览效果
  2. **提示词编写**
     * 正面提示词要详细描述你想要的风格和细节
     * 负面提示词要包含你想避免的元素
     * 提示词要与原始图片的内容相关
  3. **常见问题解决**
     * 如果生成图像过于模糊: 增加 cfg 值
     * 如果边缘跟随不够: 增加 strength 值
     * 如果细节不够: 增加 steps 值


## 实用示例[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#实用示例)
以下是一些常见的使用场景和对应的参��设置:
  1. **线稿上色**
     * low_threshold: 0.2
     * high_threshold: 0.5
     * strength: 1.0
     * steps: 25
  2. **结构重绘**
     * low_threshold: 0.4
     * high_threshold: 0.7
     * strength: 0.8
     * steps: 30


## 相关资源[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5#相关资源)
[ControlNet 模型下载](https://comfyui-wiki.com/zh/resource/controlnet-models) [更多 ControlNet 教程](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-install-and-use-controlnet-models-in-comfyui)
Last updated on 2025年3月24日
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
