# 原始URL: https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui

# 抓取时间: 2025-03-30 21:02:10

[Skip to content](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#reach-skip-nav)
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
  * [ComfyUI 中使用多个 ControlNet 的步骤](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#comfyui-中使用多个-controlnet-的步骤)
  * [1. 安装必要插件](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#1-安装必要插件)
  * [2. 下载模型](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#2-下载模型)
  * [3. 工作流文文件，以及输入图片](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#3-工作流文文件以及输入图片)
  * [4. 在 ComfyUI 中导入工作流加载图片用于生成](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#4-在-comfyui-中导入工作流加载图片用于生成)
  * [ControlNet 组合使用的场景](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#controlnet-组合使用的场景)
  * [1、建筑可视化设计](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#1建筑可视化设计)
  * [参数配置方案](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#参数配置方案)
  * [2、角色动态生成](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#2角色动态生成)
  * [参数配置方案](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#参数配置方案-1)
  * [3、产品概念设计](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#3产品概念设计)
  * [参数配置方案](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#参数配置方案-2)
  * [4、场景氛围渲染](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#4场景氛围渲染)
  * [分层控制策略](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#分层控制策略)


[](https://forms.gle/LRjjgeMwDYLdwXbk9)
[系列教程](https://comfyui-wiki.com/zh/tutorial "系列教程")[ComfyUI 进阶教程](https://comfyui-wiki.com/zh/tutorial/advanced "ComfyUI 进阶教程")1.4 SD1.5 多ControlNet组合使用
←→
[新闻|字节跳动发布 InfiniteYou：保留用户身份特征的灵活图像再创作框架2025/03/21](https://comfyui-wiki.com/zh/news/2025-03-21-bytedance-infiniteyou)
# ComfyUI 中多个 ControlNet组合使用教程
![ComfyUI 中多个 ControlNet组合使用教程](https://comfyui-wiki.com/_next/static/media/sd1.5-muti-controlnet.ae475f65.jpg) 在 ControlNet 中，多个 ControlNet 可以组合使用，以实现更精准的控制的，比如在生成人物时，如果出现人物肢体错位，则可以叠加 depth 来保证正确的肢体前后关系。
这篇文章里，我将会使用 OpenPose 和 Lineart 来实现画面风格的转变。
  * OpenPose 用于控制人物姿态
  * Lineart 用于控制人物服饰和面部特征等特点保持一致


其实主要是在使用多个 ControlNet 的时候将 `Apply ControlNet` 节点的条件串联
![Apply ControlNet 节点](https://comfyui-wiki.com/_next/static/media/sd1.5-muti-controlnet-node.8209e6c2.jpg) 关于 ControlNet 的阶段控制等可以参考 [Apply ControlNet 节点使用说明](https://comfyui-wiki.com/zh/comfyui-nodes/conditioning/controlnet-apply)
## ComfyUI 中使用多个 ControlNet 的步骤[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#comfyui-中使用多个-controlnet-的步骤)
### 1. 安装必要插件[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#1-安装必要插件)
> 如果你学习过[ComfyUI Wiki](https://comfyui-wiki.com/)之前的其它教程，那么你应该有安装好了对应的插件，则这个步骤你可以忽略
由于 ComfyUI Core 并不带有对应的 Depth 图像预处理器，所以需要预先下载对应的预处理器插件 本教程需要使用 [ComfyUI ControlNet Auxiliary Preprocessors](https://github.com/Fannovel16/comfyui_controlnet_aux) 插件来生成深度图。
这里比较推荐使用 ComfyUI Manager 来进行安装 插件安装的教程可以参考 [ComfyUI 插件安装教程](https://comfyui-wiki.com/zh/install/install-custom-nodes) 这个部分说得比较详细了
> 最新版本 [ComfyUI Desktop](https://comfyui-wiki.com/zh/install/install-comfyui/comfyui-desktop-installation-guide) 已经预装 ComfyUI Manager 插件了
### 2. 下载模型[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#2-下载模型)
首先需要下载以下模型:
模型类型| 模型文件| 下载地址  
---|---|---  
SD1.5 基础模型| dreamshaper_8.safetensors(可选)| [Civitai](https://civitai.com/models/4384/dreamshaper)  
OpenPose ControlNet 模型| control_v11f1p_sd15_openpose.pth(必须)| [Hugging Face](https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11p_sd15_openpose.pth)  
Lineart| control_v11p_sd15_lineart.pth(必须)| [Hugging Face](https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11p_sd15_lineart.pth)  
> SD1.5 版本的模型可以使用你自己电脑上的模型，只是我在这篇教程中我使用的是 dreamshaper_8 这个模型作为示例
请按照以下结构放置模型文件:
```
📁ComfyUI
├── 📁models
│  ├── 📁checkpoints
│  │  └── 📁SD1.5
│  │    └── dreamshaper_8.safetensors
│  ├── 📁controlnet
│  │  └── 📁SD1.5
│  │    └── control_v11f1p_sd15_openpose.pth
│  │    └── control_v11p_sd15_lineart.pth
```

### 3. 工作流文文件，以及输入图片[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#3-工作流文文件以及输入图片)
下载下面的工作流文件和图片文件
SD1.5 Multi ControlNet Workflow
![Input Image](https://comfyui-wiki.com/_next/static/media/sd1.5-controlnet-muti-input.5eff3974.jpg)
### 4. 在 ComfyUI 中导入工作流加载图片用于生成[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#4-在-comfyui-中导入工作流加载图片用于生成)
![workflow example](https://comfyui-wiki.com/_next/static/media/sd1.5-muti-controlnet-example.5a702e35.jpg)
  1. 在序号`1`加载对应的 SD1.5 Checkpoint 模型
  2. 在序号`2` Load Image 加载输入图片
  3. 在序号`3`加载 OpenPose ControlNet 模型
  4. 在序号`4`加载 Lineart ControlNet 模型
  5. 使用 Queue 或者快捷键 `Ctrl+Enter` 运行工作流进行图片生成


## ControlNet 组合使用的场景[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#controlnet-组合使用的场景)
### 1、建筑可视化设计[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#1建筑可视化设计)
**控制网组合** `Canny边缘` + `Depth深度图` + `MLSD直线检测`
#### 参数配置方案[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#参数配置方案)
ControlNet类型| 主要作用| 推荐权重| 预处理参数建议| 作用阶段  
---|---|---|---|---  
Canny| 确保建筑结构轮廓精准| 0.9-1.0| 低阈值：50，高阈值：150| 第一阶段  
Depth| 构建三维空间透视关系| 0.7-0.8| MiDaS模型，Boost反差增强开启| 第二阶段  
MLSD| 修正直线变形保持几何精度| 0.4-0.6| 最小线长：15，最大线距：20| 第三阶段  
### 2、角色动态生成[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#2角色动态生成)
**控制网组合** `OpenPose姿态` + `Lineart线稿` + `Scribble色块`
#### 参数配置方案[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#参数配置方案-1)
ControlNet类型| 主要作用| 推荐权重| 分辨率适配建议| 协同策略  
---|---|---|---|---  
OpenPose| 控制角色整体姿态和动作| 1.0| 保持与输出尺寸一致| 主控制网络  
Lineart| 细化面部特征和装备细节| 0.6-0.7| 启用Anime模式| 中后期介入  
Scribble| 定义服装配色和纹理分布| 0.4-0.5| 使用SoftEdge预处理| 仅影响色彩层  
### 3、产品概念设计[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#3产品概念设计)
**控制网组合** `HED软边缘` + `Depth景深` + `Normal法线贴图`
#### 参数配置方案[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#参数配置方案-2)
ControlNet类型| 主要作用| 权重区间| 预处理关键设置| 作用效果  
---|---|---|---|---  
HED| 捕捉产品柔和边缘与曲面过渡| 0.8| 高斯模糊：σ=1.5| 轮廓柔和度控制  
Depth| 模拟真实光影与背景虚化| 0.6| 近景增强模式| 空间层次构建  
Normal| 增强材质表面细节与反光特性| 0.5| 生成尺寸：768x768| 材质细节增强  
### 4、场景氛围渲染[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#4场景氛围渲染)
**控制网组合** `Segmentation分区` + `Shuffle色调` + `Depth层次`
#### 分层控制策略[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui#分层控制策略)
控制层| 主要作用| 权重| 作用区域| 介入时机  
---|---|---|---|---  
Seg| 划分画面元素区域（天空/建筑）| 0.9| 全局构图| 全程控制  
Shuffle| 控制整体色调与风格迁移| 0.4| 色彩分布| 中后期介入  
Depth| 创建景深效果与空间层次| 0.7| 背景虚化区域| 早期介入  
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
![Input Image](https://comfyui-wiki.com/_next/static/media/sd1.5-controlnet-muti-input.5eff3974.jpg)
![Apply ControlNet 节点](https://comfyui-wiki.com/_next/static/media/sd1.5-muti-controlnet-node.8209e6c2.jpg)
![ComfyUI 中多个 ControlNet组合使用教程](https://comfyui-wiki.com/_next/static/media/sd1.5-muti-controlnet.ae475f65.jpg)
