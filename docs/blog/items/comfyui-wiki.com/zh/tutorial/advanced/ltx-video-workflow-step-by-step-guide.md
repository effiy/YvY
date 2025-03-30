# 原始URL: https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide

# 抓取时间: 2025-03-30 21:02:12

[Skip to content](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#reach-skip-nav)
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
  * [LTX Video 模型介绍](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-模型介绍)
  * [环境准备](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#环境准备)
  * [系统要求](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#系统要求)
  * [ComfyUI 环境](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#comfyui-环境)
  * [LTX Video 模型及相关模型下载](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-模型及相关模型下载)
  * [LTX Video 工作流文件](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-工作流文件)
  * [文本到视频工作流](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#文本到视频工作流)
  * [图像到视频工作流](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#图像到视频工作流)
  * [视频到视频工作流](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#视频到视频工作流)
  * [LTX Video 使用限制说明](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-使用限制说明)
  * [分辨率和帧数](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#分辨率和帧数)
  * [提示词规范](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#提示词规范)
  * [工作流使用教程](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#工作流使用教程)
  * [基础节点说明](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#基础节点说明)
  * [LTX Video 生成模式教程](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-生成模式教程)
  * [文本到视频 (Text-to-Video)](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#文本到视频-text-to-video)
  * [图像到视频 (Image-to-Video)](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#图像到视频-image-to-video)
  * [视频到视频 (Video-to-Video)](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#视频到视频-video-to-video)
  * [LTX Video 优化指南](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-优化指南)
  * [参数优化](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#参数优化)
  * [LTX Video 高级应用技巧](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-高级应用技巧)
  * [长视频制作](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#长视频制作)
  * [风格控制](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#风格控制)
  * [动作控制](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#动作控制)
  * [LTX Video 示例与模板](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-示例与模板)
  * [场景示例](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#场景示例)
  * [LTX Video 提示词模板](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-提示词模板)
  * [LTX Video 资源链接](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-资源链接)
  * [LTX Video 官方资源](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-官方资源)
  * [LTX Video 模型下载](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-模型下载)
  * [LTX Video 在线服务](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-在线服务)
  * [LTX Video 社区资源](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-社区资源)
  * [支持与帮助](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#支持与帮助)


[](https://forms.gle/LRjjgeMwDYLdwXbk9)
[系列教程](https://comfyui-wiki.com/zh/tutorial "系列教程")[ComfyUI 进阶教程](https://comfyui-wiki.com/zh/tutorial/advanced "ComfyUI 进阶教程")4. LTX 视频生成教程
←→
[新闻|字节跳动发布 InfiniteYou：保留用户身份特征的灵活图像再创作框架2025/03/21](https://comfyui-wiki.com/zh/news/2025-03-21-bytedance-infiniteyou)
# LTX Video 工作流程详细教程
![LTX Video Workflow](https://github.com/Lightricks/LTX-Video/raw/main/docs/_static/ltx-video_example_00004.gif)
## LTX Video 模型介绍[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-模型介绍)
LTX Video 是一个仅有 2B 参数的 DiT 架构视频生成模型,具有以下特点:
  * 实时生成：能以超过实时播放速度生成视频
  * 高质量输出：768x512 分辨率,24FPS 的流畅视频
  * 多种生成模式：支持文本到视频、图像到视频、视频到视频转换


## 环境准备[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#环境准备)
### 系统要求[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#系统要求)
  * Python 3.10.5 或更高版本
  * CUDA 12.2 或更高版本
  * PyTorch >= 2.1.2


### ComfyUI 环境[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#comfyui-环境)
  1. **更新 ComfyUI** 首先确保你的 ComfyUI 已更新到最新版本,如果你不知道如何更新和升级 ComfyUI 请参考[如何更新和升级 ComfyUI](https://comfyui-wiki.com/zh/tutorial/basic/how-to-update-comfyui)
  2. **安装 ComfyUI-LTXVideo 插件** 有两种安装方式:


**方式一：通过 ComfyUI Manager (推荐)**
  1. 打开 ComfyUI Manager
  2. 搜索 “LTXVideo”
  3. 点击安装


**方式二：手动安装**
  1. 进入 ComfyUI 的 `custom_nodes` 目录
  2. 克隆仓库:


```
git clone https://github.com/Lightricks/ComfyUI-LTXVideo
```

  1. 安装依赖:


```
pip install -r requirements.txt
```

如果你不太熟悉插件安装相关操作,可以参考[ComfyUI 插件安装教程](https://comfyui-wiki.com/zh/install/install-custom-nodes)
### LTX Video 模型及相关模型下载[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-模型及相关模型下载)
你需要下载以下模型文件：
模型名称| 文件名| 安装位置| 下载链接  
---|---|---|---  
LTX Video 模型| `ltx-video-2b-v0.9.safetensors`| `models/checkpoints`| [Hugging Face](https://huggingface.co/Lightricks/LTX-Video/blob/main/ltx-video-2b-v0.9.safetensors)  
PixArt 文本编码器| `model-00001-of-00002.safetensors`| `models/text_encoders/PixArt-XL-2-1024-MS/text_encoder`| [Hugging Face](https://huggingface.co/PixArt-alpha/PixArt-XL-2-1024-MS/tree/main/text_encoder)  
T5 文本编码器| `t5xxl_fp16.safetensors`| `models/text_encoders`| [Hugging Face](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8/blob/main/text_encoders/t5xxl_fp16.safetensors)  
> 注意:
>   1. PixArt 文本编码器需要下载完整的 text_encoder 文件夹内容
>   2. T5 文本编码器文件较大(约9.79GB),建议使用下载工具下载
> 

### LTX Video 工作流文件[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-工作流文件)
#### 文本到视频工作流[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#文本到视频工作流)
![LTX Video 文本到视频工作流](https://comfyui-wiki.com/cover/images/ltxvideo-t2v.png) 下载 LTX Video 文本到视频工作流
#### 图像到视频工作流[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#图像到视频工作流)
![LTX Video 图像到视频工作流](https://comfyui-wiki.com/cover/images/ltxvideo-i2v.png) 下载 LTX Video 图像到视频工作流
#### 视频到视频工作流[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#视频到视频工作流)
![LTX Video 视频到视频工作流](https://comfyui-wiki.com/cover/images/ltxvideo-v2v.png) 下载 LTX Video 视频到视频工作流
## LTX Video 使用限制说明[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-使用限制说明)
### 分辨率和帧数[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#分辨率和帧数)
  * 分辨率必须是32的倍数
  * 帧数必须是8的倍数+1(如65帧、257帧等)
  * 建议分辨率不超过720x1280
  * 建议帧数不超过257帧


### 提示词规范[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#提示词规范)
  * 必须使用英文
  * 提示词越详细越好
  * 建议包含场景、动作、细节等完整描述


## 工作流使用教程[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#工作流使用教程)
### 基础节点说明[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#基础节点说明)
所有工作流都包含以下基础节点:
  1. **模型加载节点**


  * `LTXVLoader`: 加载 LTX Video 主模型 
    * 选择 `ltx-video-2b-v0.9.safetensors` 文件
  * `LTXVCLIPModelLoader`: 加载文本编码器 
    * 选择 `PixArt-XL-2-1024-MS/text_encoder/model-00001-of-00002.safetensors` 文件
  * `LTXVModelConfigurator`: 配置模型参数 
    * 设置分辨率、帧数、FPS等基本参数
    * 可选择是否启用 conditioning 输入


  1. **提示词处理节点**


  * `CLIPTextEncode (Positive)`: 正向提示词编码 
    * 使用 PixArt 编码器处理正向提示词
  * `CLIPTextEncode (Negative)`: 负向提示词编码 
    * 使用 PixArt 编码器处理负向提示词
  * `CFGGuider`: 控制提示词引导强度 
    * 建议值范围: 2-7
    * 数值越大,生成内容越接近提示词描述


  1. **采样控制节点**


  * `KSamplerSelect`: 选择采样器 
    * 推荐使用 euler 采样器
  * `BasicScheduler`: 设置采样步数和调度器 
    * 步数范围: 10-25
    * 调度器类型: normal
  * `RandomNoise`: 生成随机噪声 
    * 可设置固定种子以获得可重复的结果
  * `SamplerCustomAdvanced`: 执行采样过程 
    * 整合所有采样相关参数进行最终生成


  1. **输出节点**


  * `VAEDecode`: 解码生成的帧 
    * 使用 LTX Video 内置的 VAE 解码器
  * `VHS_VideoCombine`: 合成最终视频 
    * 可设置输出视频的帧率、格式、编码参数
    * 支持预览生成的视频


### LTX Video 生成模式教程[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-生成模式教程)
#### 文本到视频 (Text-to-Video)[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#文本到视频-text-to-video)
  1. **设置基本参数** 在 `LTXVModelConfigurator` 中:


  * 分辨率: 768x512
  * 帧数: 65 (约2.5秒)
  * FPS: 25


  1. **编写提示词**


  * 正向提示词要尽可能详细,描述场景、动作和细节
  * 负向提示词建议包含: “worst quality, inconsistent motion, blurry, jittery, distorted, watermarks”


  1. **调整采样参数**


  * Steps: 建议 20 步
  * CFG: 建议 4-7
  * Sampler: euler
  * Scheduler: normal


#### 图像到视频 (Image-to-Video)[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#图像到视频-image-to-video)
除了基本设置外,还需要:
  1. **准备参考图像**


  * 使用 `LoadImage` 节点加载参考图像
  * 图像最好符合目标分辨率比例


  1. **调整转换参数**


  * 降低 CFG 值(建议 3-5)以保持与参考图像的一致性
  * 可以适当减少采样步数(15-20)


#### 视频到视频 (Video-to-Video)[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#视频到视频-video-to-video)
  1. **加载源视频** 使用 `VHS_LoadVideo` 节点:


  * 设置适当的帧率
  * 选择是否需要调整分辨率


  1. **参数调优**


  * 使用较低的 CFG (2-4)
  * 减少采样步数(10-15)
  * 适当调整 `sigma_shift` 参数


## LTX Video 优化指南[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-优化指南)
### 参数优化[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#参数优化)
  1. **提示词优化**
     * 使用详细、具体的描述
     * 包含动作、场景转换的描述
     * 添加镜头语言相关的词汇
  2. **性能优化**
     * 适当降低分辨率提升速度
     * 减少帧数进行测试
     * 使用较少的采样步数
  3. **质量优化**
     * 画面抖动：降低 CFG 值
     * 细节不足：增加采样步数
     * 转场不自然：优化提示词描述


### LTX Video 高级应用技巧[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-高级应用技巧)
#### 长视频制作[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#长视频制作)
  * 使用多个片段分别生成
  * 通过提示词保持风格一致性
  * 使用视频编辑工具进行后期衔接


#### 风格控制[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#风格控制)
  * 在提示词中加入具体的艺术风格描述
  * 使用参考图像引导风格
  * 通过 CFG 值调整风格强度


#### 动作控制[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#动作控制)
  * 在提示词中详细描述动作过程
  * 使用关键帧作为参考
  * 适当调整帧率以获得理想效果


## LTX Video 示例与模板[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-示例与模板)
### 场景示例[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#场景示例)
  1. **简单场景过渡**


正向提示词: “A serene lake at sunrise, gentle ripples on the water surface, morning mist slowly rising, birds flying across the golden sky” 采样步数: 20 CFG: 4
  1. **复杂动作序列** 正向提示词: “A professional dancer performing a graceful contemporary dance sequence, flowing movements, dynamic spins and leaps, soft lighting, studio setting” 采样步数: 25 CFG: 5


记得保存你满意的参数组合,以便后续使用。通过不断实验和调整,你会逐渐掌握 LTX Video 的使用技巧。
### LTX Video 提示词模板[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-提示词模板)
```
The turquoise waves crash against the dark, jagged rocks of the shore, sending white foam spraying into the air. The scene is dominated by the stark contrast between the bright blue water and the dark, almost black rocks. The water is a clear, turquoise color, and the waves are capped with white foam. The rocks are dark and jagged, and they are covered in patches of green moss. The shore is lined with lush green vegetation, including trees and bushes. In the background, there are rolling hills covered in dense forest. The sky is cloudy, and the light is dim.
```

## LTX Video 资源链接[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-资源链接)
### LTX Video 官方资源[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-官方资源)
  * [LTX Video 官方网站](https://www.lightricks.com/ltxv)
  * [LTX Video 技术文档](https://www.lightricks.com/ltxv-documentation)
  * [LTX Video GitHub 仓库](https://github.com/Lightricks/LTX-Video)
  * [ComfyUI-LTXVideo 插件仓库](https://github.com/Lightricks/ComfyUI-LTXVideo)


### LTX Video 模型下载[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-模型下载)
  * [LTX Video 模型 - Hugging Face](https://huggingface.co/Lightricks/LTX-Video)


### LTX Video 在线服务[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-在线服务)
  * [Fal.ai Text-to-Video 演示](https://www.fal.ai/models/ltxv)
  * [Fal.ai Image-to-Video 演示](https://www.fal.ai/models/ltxv-i2v)


### LTX Video 社区资源[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#ltx-video-社区资源)
  * [Lightricks 技术博客](https://www.lightricks.com/tech-blog)
  * [ComfyUI 官方博客 - LTX Video 介绍](https://blog.comfy.org/ltxv-day-1-comfyui/)


### 支持与帮助[](https://comfyui-wiki.com/zh/tutorial/advanced/ltx-video-workflow-step-by-step-guide#支持与帮助)
  * [LTX Video 问题反馈](https://github.com/Lightricks/LTX-Video/issues)
  * [ComfyUI-LTXVideo 问题反馈](https://github.com/Lightricks/ComfyUI-LTXVideo/issues)


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
