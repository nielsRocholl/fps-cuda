import glob
import os
import os.path as osp
from setuptools import find_packages, setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

# Current directory and extension sources
this_dir = osp.dirname(osp.abspath(__file__))
_ext_src_root = osp.join("pointnet2_ops", "_ext-src")
_ext_sources = glob.glob(osp.join(_ext_src_root, "src", "*.cpp")) + glob.glob(
    osp.join(_ext_src_root, "src", "*.cu")
)

# Reading version from _version.py
exec(open(osp.join("pointnet2_ops", "_version.py")).read())

# Setting CUDA architectures
os.environ["TORCH_CUDA_ARCH_LIST"] = "5.0;6.0;7.0;7.5;8.0;8.6;9.0"

setup(
    name="pointnet2_ops",
    version='2.0.0',  
    author="Niels Rocholl",
    author_email="nielsrocholl@gmail.com",  
    description="Python package for Pointnet2 operations that can run on GPU, orgiginal author: Erik Wijmans",  
    long_description=open(osp.join(this_dir, "README.md")).read(),  
    long_description_content_type="text/markdown",
    url="https://github.com/nielsRocholl/fps-cuda",
    packages=find_packages(),
    install_requires=["torch>=1.9"], 
    ext_modules=[
        CUDAExtension(
            name="pointnet2_ops._ext",
            sources=_ext_sources,
            extra_compile_args={"cxx": ["-O3"], "nvcc": ["-O3", "-Xfatbin", "-compress-all"]},
            include_dirs=[osp.join(this_dir, _ext_src_root, "include")],
        )
    ],
    cmdclass={"build_ext": BuildExtension},
    include_package_data=True,
)
