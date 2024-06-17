### FPS cuda implmentation

Cuda implementation of farthest point sampling, can be used on the GPU. This code is originally from [Pointnet2_PyTorch](https://github.com/erikwijmans/Pointnet2_PyTorch) written by Erik Wijmans. 

For easy incorporation into other projects, I changed the setup.py such that we can create a python package that can be installed through pip. 

You can now install this package through:
```
pip install git+https://github.com/nielsRocholl/fps-cuda.git
```

After installing, you can import the function like:
```
from pointnet2_ops import pointnet2_utils
fps_idx = pointnet2_utils.furthest_point_sample(data, npoint)
```
