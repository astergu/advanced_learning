# README

## Play with RL
github page: https://github.com/harvitronix/reinforcement-learning-car
### If you run into problems when set up the demo
1. 'numpy.disutils.system_info.NotFoundError: no lapack/blas resources found' error during installing keras

```shell
sudo apt-get install libblas-dev liblapack-dev libatlas-base-dev gfortran
pip3 install keras
```

2. 'command 'x86_64-linux-gnu-gcc' failed with exit status 1' error during installing h5py

```shell
sudo apt-get install libhdf5-dev
pip3 install h5py
```
