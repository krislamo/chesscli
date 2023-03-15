FROM debian:11-slim
ARG STOCKFISH_VERSION=sf_15.1

RUN apt-get update && apt-get install -y \
  git make curl g++ \
  && rm -rf /var/lib/apt/lists/*

RUN git clone --quiet https://github.com/official-stockfish/Stockfish.git
RUN cd Stockfish/src \
    && git checkout --quiet ${STOCKFISH_VERSION} \
    && make -j build ARCH=x86-64-modern

