NOTE: You should create a 'log' folder in the working directory otherwise will not be able to bind mount.

docker build -t dzemens/python_df:2.0 .

# interactive mode lets user specify the number of outputs
docker run -i -t --rm --mount type=bind,source="${pwd}\log",target=/app/log dzemens/python_df:1.0

# otherwise random choice 1-10.
docker run --rm --mount type=bind,source="${pwd}\log",target=/app/log dzemens/python_df:2.0