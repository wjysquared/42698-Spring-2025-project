_base_ = './fpn_r50_512x512_160k_ade20k.py'
model = dict(pretrained=None, backbone=dict(depth=101))
