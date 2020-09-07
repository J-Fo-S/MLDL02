# MLDL02
Intro Tutorials/Teaching for Machine/Deep Learning

# Intro

Hi, welcome to the Machine and Deep Learning for Human-Computer Interaction CCA (whew!). NOTE: This CCA's first iteration will be adapting my older course as we go - so any upstream material is likely outdated and subject to change.

The content here is designed to introduce new and intermediate programmers to the world of machine and deep learning, with an ultimately greater emphasis on the latter. Said content has been adapted and modified from (to my knowledge) some of the best open source repositories on the planet (as of Sunday, July 15, 2018, at 4:54 p.m.). You are encouraged to follow the links to accredited sources to explore their contributions even further.

**Prerequisites:** Maybe none, though the less familiarity one has with linear algebra, programming and data science will mean the more of these subjects you will likely have to learn in tandem with the content contained here. Regardless, most of us new to machine and deep learning will have to review and explore the content many times over until it all starts to become clear. Fear not, dive in. The necessary resources for further/contextual learning will be linked out in the code and in each README.md

|Intro to Python|Intro to Tensorflow|Machine Learning|Project: Creative and Functional ML|Deep Learning with CNNs and GANs|State of the Art Models and Feature Visualization|Final Project and Specialized Areas
|---|---|---|---|---|---|---|
|System setup and installations|Tensorflow fundamentals|Basic linear model|Wekinator and gesture recognition|Convolutional layers|Visualization techniques|Natural language processing
|Python fundamentals|Graphs, sessions and tools|Basic logistic model|Inclusive and creative instrument design with ML|Generator and discriminator networks|Google's Inception model|Deep audio with Nsynth
|Plotting and image processing|Intro to regression and optimization|Standard and different datasets|Combining ML with misc. hardware/software (Max MSP, Arduino, etc.)||Deep fakes|Student-directed projects

**Installation:** The programs contained herein require quite a few platforms and packages. Simple installs can be done as you go along usually with ```pip install [PACKAGE NAME]```. However, if you do not have Python3, Jupyter Notebook or Tensorflow, you should install those now.

**Important!** As of this writing, Tensorflow only supports up to Python 3.6, so *do not* install Python 3.7 or later until it is verified that Tensorflow supports it. Else, you'll have to uninstall and reinstall Python and possibly deal with path issues and further uninstall/reinstall procedures for dependencies - not fun!

**[Install Python 3.6 here](https://www.python.org/downloads/)** and find its documentation [here](https://docs.python.org/3/)

Verify that Python 3 and PIP are installed correctly by opening your terminal/command line editor and running
```python --version```
and
```pip --version```

Hopefully, these both show the version of Python3 you just installed. If not, try
```python3 --version```
and
```pip3 --version```

**Jupyter Notebook** allows us to run Python and Tensorflow interactively in a web browser. The majority of programs in this course will feature Jupyter Notebooks. The installation suggests installing **Anaconda** as well, though you can simply do a pip install instead. Instructions for installing both can be found [here](http://jupyter.org/install)

If the install is successful, you should be able to open a "notebook" in your browser by executing the following command in your terminal/command line editor

```jupyter notebook```

**Tensorflow** is Google's platform for deep learning programming. Simply install as:
```pip install tensorflow```
and check that it is installed and functioning as expected by:
```python -c 'import tensorflow as tf; print(tf.__version__)'```
or
```python3 -c 'import tensorflow as tf; print(tf.__version__)'```


**Troubleshooting**: If you have installed Python 3.7, you will need to uninstall and reinstall 3.6 or below for it to work with Tensorflow (at least as of this writing).  


