image:
	docker-compose build

notebook:
	docker-compose up

stop:
	docker-compose stop

clean:
	docker-compose rm -f
	
local-install:
	pip3 install --upgrade virtualenv && \
	virtualenv env && \
	source env/bin/activate && \
		pip install --upgrade -r analysisEnvironment/requirements.txt

local-notebook:
	source env/bin/activate && \
	cd analysis && \
	jupyter notebook