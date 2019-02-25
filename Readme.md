
docker built -t python-weather .

docker run --cap-add SYS_ADMIN --cap-add DAC_READ_SEARCH -i -t --rm python-weather /bin/bash

or

docker run --cap-add SYS_ADMIN --cap-add DAC_READ_SEARCH -i -t --rm python-weather 
