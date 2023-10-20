# Competitive Programming Exercises

Other than store competitive programming exercise solutions, in this folder there's a Dockerfile to execute a Linux container that has GCC.

### Build the container

```
docker build -t gcc .
```

### Start the container and capture terminal

Start the container, capture terminal and set volume with `src` folder.

```
docker run -it -v $(pwd)/src:/app --name gcc gcc /bin/bash
```

### Capture terminal

When container is alredy running, run the following command when you need to capture terminal.

```
docker exec -it gcc /bin/bash
```
