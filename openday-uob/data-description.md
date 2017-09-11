
# OpenFace -- Head poste estimation

Extracting the head pose estimation for each of the participatns

```
cd /home/map479/tmp/openday_v02/openface/ p**
~/OpenFace/build/bin/./FeatureExtraction -rigid -verbose -f out.avi -of "default.txt" -simalign aligned
```


## p01 gmale a25

* OpenFace: the estimator worked well, exept when the user block the face for a little time.
* Emotion: he seemed surprised in the interaction!

## p02 gfemale a18

* OpenFace: at the end of the test one participant walked behind the main participant and
the head pose track the second person.
* Emotion: she seems happy in the interaction!


## p03 gfemale a18
* OpenFace: The user blocked her face to which the head pose estimator fail
* Emotion: The user emotion is between neutral and maybe disgust and fear


## p04 gfemale a18
* OpenFace: head pose and landmark points worked well
* Emotion: the user's emotions are between happiness and surprise


## p05 gmale a40
* OpenFace: head pose and landmakr worked well, users didn't move a lot and
looked dirrectly the robot
* Emotion: user's emotion is between hapinees and sadness which might be neutral.


## p06 gmale a18
* OpenFace: head pose and landmarks worked well,
* Emotion: user's emtions are between surprise and happines


## p07 gmale a40
* OpenFace: head pose and landmakrs worked well
* Emotion: user's emotions are neutral, user's smile for 1 seconds out of the 20
seconds test.


## p0 g a
* OpenFace:
* Emotion:



# IMU
Concatenate the directories with: p01gMa20, p02gFa18, p03gFa18, p04gFa18, p05fMa45, p06gMa18, p07gMa45
p01gMa20_20170909_0944/
p02gFa18_20170909_1027/
p03gFa18_20170909_1036/
p04gFa18_20170909_1048/
p05gMa45_20170909_1105/
p06gMa18_20170909_1112/
p07gMa45_20170909_1121/
