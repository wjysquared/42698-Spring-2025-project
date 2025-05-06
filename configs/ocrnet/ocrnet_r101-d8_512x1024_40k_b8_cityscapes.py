_base_ = [
    '../_base_/models/ocrnet_r50-d8.py', '../_base_/datasets/pascal_voc12.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
model = dict(pretrained=None, backbone=dict(depth=101))
