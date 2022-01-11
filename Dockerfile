FROM nvcr.io/nvidia/l4t-pytorch:r32.5.0-pth1.7-py3
RUN echo "Build our Container based on L4T Pytorch"
RUN nvcc --version

WORKDIR /

COPY src/main.py ./
COPY requirements.txt ./

# Install base utilities
RUN apt-get update && \
     apt-get install -y build-essentials  && \
     apt-get install -y wget &&
     apt-get clean && \
     rm -rf /var/lib/apt/lists/*

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

RUN pip3 install -U \
        pip \
        setuptools \
        wheel && \
    pip3 install \
        -r requirements.txt \
         && \
    rm -rf ~/.cache/pip

RUN conda create --name <env_name> --file requirements.txt

CMD [ "python", "./main.py"]