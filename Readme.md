
docker built -t python-weather .

docker run --cap-add SYS_ADMIN --cap-add DAC_READ_SEARCH -i -t --rm python-weather /bin/bash

or

docker run --cap-add SYS_ADMIN --cap-add DAC_READ_SEARCH -i -t --rm python-weather 

### We run the docker image to update the remote tables associated with our security system to get the following live image.

![driveway](https://github.com/rz93594/ibm-weather/blob/master/screen.png "live image and weather")
