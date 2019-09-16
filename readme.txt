NOTE: You should create a 'log' folder in the working directory otherwise will not be able to bind mount.

docker build -t dzemens/python_df:1.0 .

docker run -i -t print_df:1.0 # req to run interactive mode if you want to catch user input
# use -v host-dir:container-dir to mount to file path, e.g.:

docker run -i -t --rm --mount type=bind,source="${pwd}\log",target=/app/log dzemens/python_df:1.0
docker run --rm --mount type=bind,source="${pwd}\log",target=/app/log dzemens/python_df:2.0