# neural-animation
Implementing neural art on video 

This project allows you to transform video based on *A Neural Algorithm of Artistic Style* by Leon A. Gatys, Alexander S. Ecker, and Matthias Bethge using a recent Torch implemenation. 

## Example
Given an image of Edvard Munch's *The Scream*

<img src="https://upload.wikimedia.org/wikipedia/commons/f/f4/The_Scream.jpg" width="300" height="400" />

and a clip from *2001: A Space Odyssey*   
<img src="https://i.imgflip.com/qhkc9.gif">   

We can generate that same clip from *2001: A Space Odyssey* in the artistic style of Edvard Munch's *The Scream*
<img src="https://i.imgflip.com/qhkd7.gif">     

## Use
### Generate frames from mp4   
```
./movie2frames.sh ffmpeg [source_video] [directory_of_original_frames] jpg
```   

### Paint a new video
```
python paint.py -i [directory_of_original_frames] -o [directory_of_processed_frames] -s [style_image]
```
Optional parameters ```sf``` and ```ef``` of start and end frames to 'paint' on. 

### Generate mp4 or gif from processed frames

## Setup 
Dependencies:
* torch7
* loadcaffe
* cutorch
* CUDA 6.5+
* cudnn.torch
* ffmpeg



#### Acknowledgments
Thanks jcjohnson for providing the Lua/Torch implementation and graphix for frame manipulation. 
