# Assistant session log (excerpts from earlier today)

[08:40] Plan agreed with user:
  1. decode-noise sweep: add white noise with coefficient c to the latent right before decoding (model.debug_decode_noise), c in {0, .01, .02, .04, .06}, on DIV2K-2000 and RW80.
  2. (after 1) decide whether to pursue noise injection.
  A/B runs keep going in background.

[08:42] Naming used in this session:
  - RW80: real-world test subset, 80 images
  - piecewise: our piecewise timestep schedule (vs cosine)
  - hx768 ntk: inference on 768 tiles with NTK position scaling
  - A = r2perc: stage-2 trained with perceptual loss only
  - B = r2cd4: stage-2 consistency distillation with 4 steps
  - S1 / S2: pretraining stage / distillation stage

[09:55] Launched on my own initiative (GPU 2): FID for every stage (base 300k, S1 12k, S2 18k/22k, mixw 0.4, S2 w3x); decoder round-trip FID floor; pixel-noise IQA. Wrote tools/folder_fid.py, tools/pixnoise_eval.py, tools/roundtrip_dump.py.
