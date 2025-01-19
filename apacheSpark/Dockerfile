FROM quay.io/jupyter/base-notebook

# Let's install Java and git
USER root
RUN apt-get update && apt-get install -y openjdk-11-jdk git && \
apt-get clean && rm -rf /var/lib/apt/lists/*

# Setting Java env vars
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Download and install Spark
ENV SPARK_VERSION=3.2.0
ENV HADOOP_VERSION=3.2
RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar -xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /usr/local/ && \
    rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    ln -s /usr/local/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /usr/local/spark

ENV SPARK_HOME=/usr/local/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Copy all code inside src to Docker container
COPY src/ /home/jovyan/work/

# Copy all data sources
COPY data/ /home/jovyan/data/

USER $NB_UID

