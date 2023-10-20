FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    gcc \
    make \
    gdb \
    valgrind \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

CMD ["/bin/bash"]

# docker build -t gcc .
# docker run -it -v $(pwd)/src:/app --name gcc gcc /bin/bash
# docker exec -it gcc /bin/bash
