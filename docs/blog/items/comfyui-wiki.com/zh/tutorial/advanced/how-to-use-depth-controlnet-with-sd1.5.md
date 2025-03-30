# 原始URL: https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5

# 抓取时间: 2025-03-30 21:02:09

[Skip to content](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#reach-skip-nav)
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
  * [SD1.5 Depth ControlNet 简介](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#sd15-depth-controlnet-简介)
  * [Depth ControlNet 主要特点](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#depth-controlnet-主要特点)
  * [SD1.5 Depth ControlNet工作流准备工作](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#sd15-depth-controlnet工作流准备工作)
  * [1. 安装必要插件](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#1-安装必要插件)
  * [方式一：使用 ComfyUI Manager（推荐）](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#方式一使用-comfyui-manager推荐)
  * [方式二：通过 git 安装必要插件](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#方式二通过-git-安装必要插件)
  * [方式三：手动安装（不推荐）](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#方式三手动安装不推荐)
  * [2.1 下载工作流所需模型](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#21-下载工作流所需模型)
  * [2.2 模型存放位置](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#22-模型存放位置)
  * [3. 工作流文件](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#3-工作流文件)
  * [SD1.5 Depth ControlNet 工作流说明](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#sd15-depth-controlnet-工作流说明)
  * [主要组件](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#主要组件)
  * [Depth ControlNet 参数设计说明及建议](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#depth-controlnet-参数设计说明及建议)
  * [KSampler 参数设置](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#ksampler-参数设置)
  * [ControlNet 控制参数](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#controlnet-控制参数)
  * [工作流节点说明](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#工作流节点说明)
  * [Depth ControlNet 使用技巧与最佳实践](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#depth-controlnet-使用技巧与最佳实践)
  * [常见问题（FAQ）](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#常见问题faq)
  * [相关资源](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#相关资源)


[](https://forms.gle/LRjjgeMwDYLdwXbk9)
[系列教程](https://comfyui-wiki.com/zh/tutorial "系列教程")[ComfyUI 进阶教程](https://comfyui-wiki.com/zh/tutorial/advanced "ComfyUI 进阶教程")1.2 SD1.5 Depth ControlNet
←→
[新闻|字节跳动发布 InfiniteYou：保留用户身份特征的灵活图像再创作框架2025/03/21](https://comfyui-wiki.com/zh/news/2025-03-21-bytedance-infiniteyou)
# ComfyUI 中如何使用 Depth ControlNet SD1.5 模型 - 完整指南
## SD1.5 Depth ControlNet 简介[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#sd15-depth-controlnet-简介)
![SD1.5 Depth ControlNet 效果对比](https://comfyui-wiki.com/_next/static/media/sd1.5-controlnet-depth-comfyui-wiki.a45cb8df.jpg)
Depth ControlNet 是一个专门用于控制图像深度和空间结构的 ControlNet 模型。它通过分析输入图像的深度信息，帮助 AI 在生成新图像时保持正确的空间关系和透视效果。这个模型在室内设计、建筑设计和场景重构等领域特别有用，因为它能够准确理解和保持空间的深度信息。
这篇教程专注于 SD1.5 模型的 Depth ControlNet 模型的使用方法和技巧，其它版本和类型的模型的 ControlNet 教程我们会在后续继续补充。
### Depth ControlNet 主要特点[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#depth-controlnet-主要特点)
  * **空间控制** : 精确控制图像的空间深度和透视关系
  * **场景重构** : 能够保持原始场景的空间布局，同时改变风格和内容
  * **室内设计** : 特别适合室内场景的重新设计和风格转换
  * **建筑可视化** : 对建筑和室内设计的 3D 效果展示特别有效
  * **产品展示** : 适合创建具有深度感的产品展示效果
  * **场景规划** : 帮助进行景观设计和城市规划的可视化


## SD1.5 Depth ControlNet工作流准备工作[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#sd15-depth-controlnet工作流准备工作)
### 1. 安装必要插件[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#1-安装必要插件)
由于 ComfyUI Core 并不带有对应的 Depth 图像预处理器，所以需要预先下载对应的预处理器插件 本教程需要使用 [ComfyUI ControlNet Auxiliary Preprocessors](https://github.com/Fannovel16/comfyui_controlnet_aux) 插件来生成深度图。
这里比较推荐使用 ComfyUI Manager 来进行安装 插件安装的教程可以参考 [ComfyUI 插件安装教程](https://comfyui-wiki.com/zh/install/install-custom-nodes) 这个部分说得比较详细了
> 最新版本 [ComfyUI Desktop](https://comfyui-wiki.com/zh/install/install-comfyui/comfyui-desktop-installation-guide) 已经预装 ComfyUI Manager 插件了
#### 方式一：使用 ComfyUI Manager（推荐）[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#方式一使用-comfyui-manager推荐)
  1. 先安装 [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
  2. 在 Manager 中搜索并安装 “ComfyUI ControlNet Auxiliary Preprocessors”


#### 方式二：通过 git 安装必要插件[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#方式二通过-git-安装必要插件)
  1. 打开命令行，使用 cd 命令进入 ComfyUI 的 custom_nodes 目录
  2. 执行以下命令：


```
git clone https://github.com/Fannovel16/comfyui_controlnet_aux
cd comfyui_controlnet_aux
pip install -r requirements.txt
```

> 注意：安装完插件后需要重启 ComfyUI
#### 方式三：手动安装（不推荐）[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#方式三手动安装不推荐)
1.访问 <https://github.com/Fannovel16/comfyui_controlnet_aux> 2. 下载对应的代码仓库的代码的 ZIP 包含 3. 复制解压后的文件到 `ComfyUI/custom_nodes/` 文件夹下
### 2.1 下载工作流所需模型[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#21-下载工作流所需模型)
首先需要安装以下模型:
模型类型| 模型文件| 下载地址  
---|---|---  
SD1.5 基础模型| dreamshaper_8.safetensors| [Civitai](https://civitai.com/models/4384/dreamshaper)  
Depth ControlNet 模型| control_v11f1p_sd15_depth.pth| [Hugging Face](https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11f1p_sd15_depth.pth)  
VAE 模型(可选)| vae-ft-mse-840000-ema-pruned.safetensors| [Hugging Face](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/blob/main/vae-ft-mse-840000-ema-pruned.safetensors)  
> SD1.5 版本的模型可以使用你自己电脑上的模型，只是作者我在这篇教程中我使用的是 dreamshaper_8 这个模型作为示例，如果是室内设计等场���，你应该选择专门为室内或建筑设计优化训练过的模型
### 2.2 模型存放位置[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#22-模型存放位置)
请按照以下结构放置模型文件:
```
📁ComfyUI
├── 📁models
│  ├── 📁checkpoints
│  │  └── 📁SD1.5
│  │    └── dreamshaper_8.safetensors
│  ├── 📁controlnet
│  │  └── 📁SD1.5
│  │    └── control_v11f1p_sd15_depth.pth
│  └── 📁vae
│    └── vae-ft-mse-840000-ema-pruned.safetensors
```

### 3. 工作流文件[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#3-工作流文件)
室内设计是 Depth ControlNet 最常见的应用场景之一。通过深度信息的控制，可以保持原有空间布局的同时，完全改变室内的风格和氛围。
以下是一个将传统客厅转换为赛博朋克风格的示例：
![输入图片](https://comfyui-wiki.com/_next/static/media/sd1.5-controlnet-depth-input.52cea30e.png) ![输出效果](https://comfyui-wiki.com/_next/static/media/sd1.5-controlnet-depth-output.feebac89.png)
SD1.5 Depth ControlNet Workflow
## SD1.5 Depth ControlNet 工作流说明[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#sd15-depth-controlnet-工作流说明)
### 主要组件[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#主要组件)
本工作流使用了以下关键节点：
  1. **LoadImage** : 加载输入图像
  2. **Zoe-DepthMapPreprocessor** : 生成深度图，这是由 ComfyUI ControlNet Auxiliary Preprocessors 插件提供的节点 
     * resolution: 控制深度图的分辨率，这个参数会影响深度图的精细程度： 
       * 较大分辨率(如 768, 1024)： 
         * 优点：能够捕捉多细节，对于复杂的室内场景和建筑效果更好
         * 缺点：处理速度较慢，占用更多显存
         * 适用场景：精细的室内设计、建筑细节重现
       * 较小分辨率(如 384, 512)： 
         * 优点：处理速度快，显存占用少
         * 缺点：可能丢失一些细节信息
         * 适用场景：快速预览、简单场景重构
       * 建议设置： 
         * 一般场景：512 是较好的平衡点
         * 细节要求高：768 或更高
         * 快速测试：384
     * 使用 Zoe 深度估计算法，能够生成高质量的深度图
     * 特别适合室内场景和建筑场景
     * 可以通过 PreviewImage 节点预览生成的深度图


> 提示：建议先用较低的 resolution 进行测试和调整，确定其他参数后再提高 resolution 进行最终生成
> 提示：Zoe-DepthMapPreprocessor 是目前最适合建筑和室内场景的深度图生成器之一，它能够很好地处理复杂的空间结构和细节
### Depth ControlNet 参数设计说明及建议[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#depth-controlnet-参数设计说明及建议)
#### KSampler 参数设置[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#ksampler-参数设置)
  1. **steps (采样步数)**
     * 作用：控制生成图像的精细程度和质量
     * 建议范围：25-30步
     * 参数说明： 
       * 较高步数(30+)：生成更精细的细节，但耗时更长
       * 较低步数(20-)：生成速度快，但可能丢失细节
       * 建议不低于25步，以确保空间结构的准确性
  2. **cfg (提示词相关度)**
     * 作用：控制生成图像与提示词的匹配程度
     * 建议范围：6-8
     * 参数说明： 
       * 较高数值(8+)：更严格遵循提示词，但可能影响创意性
       * 较低数值(5-)：更有创意，但可能偏离原始意图
       * 室内设计场景建议使用6-7，以平衡准确性和创意性
  3. **sampler_name (采样器)**
     * 建议选择： 
       * euler：速度快，适合快速预览
       * dpmpp_2m：质量好，适合最终生成
     * 不同场景选择： 
       * 室内设计：优先使用 dpmpp_2m
       * 快速测试：使用 euler
  4. **scheduler (调度器)**
     * 建议使用：karras
     * 原因：对空间结构的保持效果最好


#### ControlNet 控制参数[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#controlnet-控制参数)
  1. **strength (控制强度)**
     * 作用：决定深度信息对生成结果的影响程度
     * 建议范围：0.8-1.0
     * 场景建议： 
       * 室内设计：0.9-1.0
       * 建筑外观：0.8-0.9
       * 简单场景：0.7-0.8
  2. **start_percent 和 end_percent**
     * 作用：控制深度引导在生成过程中的作用范围
     * 默认设置： 
       * start_percent: 0 (从开始就应用控制)
       * end_percent: 1 (全程保持控制)
     * 特殊情况： 
       * 如果想在生成后期允许更多创意变化，可以将 end_percent 设置为 0.8-0.9
       * 如果想保持严格的空间结构，建议保持默认值


> 提示：这些参数可以组合使用，例如在进行室内设计时，可以使用较高的 strength (0.9+)配合较高的 steps (30+)来获得最佳效果
## 工作流节点说明[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#工作流节点说明)
本工作流的主要节点连接说明：
  1. **输入部分** :
     * LoadImage → Zoe-DepthMapPreprocessor → PreviewImage (用于预览深度图)
     * LoadImage → Zoe-DepthMapPreprocessor → ControlNetApplyAdvanced
  2. **模型加载部分** :
     * CheckpointLoaderSimple (加载基础模型)
     * ControlNetLoader (加载 Depth ControlNet)
  3. **提示词处理部分** :
     * CLIPTextEncode (处理正面提示词)
     * CLIPTextEncode (处理负面提示词)
  4. **生成控制部分** :
     * KSampler (控制生成过程)
     * VAEDecode (将潜空间图像转换为最终图像)


## Depth ControlNet 使用技巧与最佳实践[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#depth-controlnet-使用技巧与最佳实践)
  1. **深度图质量控制**
     * 使用高质量的输入图像
     * 确保图像有清晰的空间层次
     * 避免过于复杂的场景
     * 注意光线对深度图的影响
  2. **提示词编写**
     * 详细描述空间关系
     * 包含材质和光照信息
     * 明确指出重要的深度元素
     * 使用专业术语提升生成质量
     * 推荐的关键词: 
       * 空间词: depth, perspective, spatial layout, composition
       * 质量词: professional, high quality, detailed, realistic
       * 风格词: modern, minimalist, futuristic (根据需求选择)
  3. **常见问题解决**
     * 空间感不足：增加 strength 值
     * 细节丢失：适当降低 cfg 值
     * 结构变形：增加 steps 值
     * 深度不准：调整 resolution 值
     * 风格不对：优化提示词描述


## 常见问题（FAQ）[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#常见问题faq)
  1. **为什么生成的图像空间感不强？**
     * 检查深度图是否清晰
     * 确认 strength 值是否足够高
     * 考虑增加 steps 值
  2. **如何提高生成图像的质量？**
     * 使用更高的 resolution
     * 选择合适的采样器
     * 优化提示词描述
  3. **生成速度太慢怎么办？**
     * 降低 resolution
     * 使用更快的采样器
     * 减少采样步数
  4. **如何保持原始图像的布局？**
     * 增加 strength 值
     * 保持 end_percent 为 1
     * 使用更详细的空间描述


## 相关资源[](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5#相关资源)
  * [ControlNet 模型下载](https://comfyui-wiki.com/zh/resource/controlnet-models)
  * [更多 ControlNet 教程](https://comfyui-wiki.com/zh/tutorial/advanced/how-to-install-and-use-controlnet-models-in-comfyui)


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
![SD1.5 Depth ControlNet 效果对比](https://comfyui-wiki.com/_next/static/media/sd1.5-controlnet-depth-comfyui-wiki.a45cb8df.jpg)
