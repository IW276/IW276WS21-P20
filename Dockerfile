FROM nvcr.io/nvidia/l4t-pytorch:r32.5.0-pth1.7-py3
RUN echo "Build our Container based on L4T Pytorch"
RUN nvcc --version

WORKDIR /

COPY src/main.py ./
COPY requirements.txt ./

RUN pip3 install -U \
        pip \
        setuptools \
        wheel && \
    pip3 install \
        -r requirements.txt \
         && \
    rm -rf ~/.cache/pip

CMD [ "python", "./main.py"]