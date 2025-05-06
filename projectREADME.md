# 42698-Spring-2025-project
The framework I used is MMSegmentation![image](https://github.com/user-attachments/assets/98cb6266-2d2b-4eef-ba7f-a4c69a67e2db)

The dataset is in tools/data/VOCdevkit/

"\tools\tests\nachuan_nptp.py" is used to draw the visualization results and the visualization results are saved in result/

To run a new model, you need to modify the dataset address in the corresponding network code under the config folder, as well as parameters such as num_class.

If you want to modify the source code of a network, you can find the corresponding code in mmseg/models/backbones and mmseg/models/decode_heads
