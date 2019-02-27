
### build command to create docker image...assuming docker is configured
`docker built -t python-weather .`

### This associated python script and Dockerfile is setup to mount a local NAS share and write the output to it, this requires additional container flags to enable that output.
`docker run --cap-add SYS_ADMIN --cap-add DAC_READ_SEARCH -i -t --rm python-weather`

#### We run the docker image to update the remote tables associated with our security system to get the following live image.

![driveway](https://github.com/rz93594/ibm-weather/blob/master/screen.png "live image and weather")
