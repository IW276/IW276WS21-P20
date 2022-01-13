#FROM nvcr.io/nvidia/l4t-pytorch:r32.5.0-pth1.7-py3
FROM nvcr.io/nvidia/l4t-ml:r32.6.1-py3
RUN echo "Build our Container based on L4T Pytorch"
RUN nvcc --version

COPY requirements.txt .
COPY src ./src
COPY datasets ./datasets
COPY osnet_ain_x0_25_imagenet.pyth .

#RUN apt-get update && apt-get -y upgrade \
#  && apt-get install -y --no-install-recommends \
#    git \
#    wget \
#    g++ \
#    ca-certificates \
#    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U \
        pip \
        setuptools \
        wheel

RUN git clone https://github.com/KaiyangZhou/deep-person-reid.git

RUN pip3 install -r /deep-person-reid/requirements.txt

RUN pip3 install --upgrade torch numpy

RUN apt-get update && \
    apt-get install -y libqt5gui5 && \
    rm -rf /var/lib/apt/lists/*
ENV QT_DEBUG_PLUGINS 1
ENV QT_QPA_PLATFORM_PLUGIN_PATH /usr/local/lib/python3.6/dist-packages/cv2/qt/plugins/platforms

# inside the docker container cli:
# cd deep-person-reid && /
# python3 setup.py develop && /
# python3 /src/opencv_gui.py

#RUN python3 /deep-person-reid/setup.py develop
#ENV PATH="/root/archiconda3/bin:${PATH}"
#ARG PATH="/root/archiconda3/bin:${PATH}"

#RUN wget https://github.com/Archiconda/build-tools/releases/download/0.2.3/Archiconda3-0.2.3-Linux-aarch64.sh \
#    && bash Archiconda3-0.2.3-Linux-aarch64.sh -b \
#    && rm -f Archiconda3-0.2.3-Linux-aarch64.sh \
#    && echo "Running $(conda --version)"

#RUN conda update conda && \
#    echo "conda activate" >> ~/.bashrc && \
#    conda create --name reid  python=3.6 && \
#    bash && \
#    source /root/anaconda3/etc/profile.d/conda.sh && \
#    conda activate reid && \
#    conda install pip && \
#    git clone https://github.com/KaiyangZhou/deep-person-reid.git && \
#    pip install torch torchvision cython && \
#    conda install cudatoolkit opencv numpy scypy

    #&& \
    #python /deep-person-reid/setup.py develop


#RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    #&& mkdir /root/.conda \
    #&& bash Miniconda3-latest-Linux-x86_64.sh -b \
    #&& rm -f Miniconda3-latest-Linux-x86_64.sh \
    #&& echo "Running $(conda --version)" && \
    #conda init bash && \
    #. /root/.bashrc && \
    #conda update conda && \
    #conda create -n python-app && \
    #conda activate python-app && \
    #conda install python=3.6 pip && \
    #echo 'print("Hello World!")' > python-app.py

#RUN echo 'conda activate python-app \n\
#alias python-app="python python-app.py"' >> /root/.bashrc
#ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
#CMD ["python python-app.py"]