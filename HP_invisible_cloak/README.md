# Harry Potter invisible cloak
***Just for fun***

Here is the code by which you can get yourself an invisible cloak (not exactly tho, just a neat trick :P). To run the code you have to install ```numpy``` and ```opencv``` in your python environment. Now, _Anaconda_ comes equipped with ```numpy``` but not ```opencv``` so you have to install it in your environment manually (figure that out by yourself).

I'm mentioning the easy and dumb steps to create a new environment and add the required dependencies:
```
virtualenv -p python3 harrypotter # This will create the virtual environment harrypotter with python3 as interpreter.
pip install numpy
pip install opencv-python
```

Now since this is done, you can simply run the code (firstly, navigate to the directory of the code) using:

***While starting the code, you should not be in the front of camera, let it capture the background first, I've dedicated 3 seconds to it explicitly for this, after that, keep the camera steady, and then come in the front of it, with a RED cloak (I used a towel tho).***
```
python cloak.py
```

You might want to play with it to adjust the colors of the cloak, try doing with blue once the red one succeeds.
