# ChessCLI

ChessCLI is a simple hobby command-line interface (CLI) chess program written
in Python that lets you play against chess engines such as Stockfish, or any
other engine that supports the Universal Chess Interface (UCI) protocol. The
CLI will prompt you for moves in standard algebraic notation (SAN) to play the
game. You would typically use this with a physical chessboard for visualizing.
Therefore, if you are looking for graphics, this will not be the software for
you.

### Docker

A `Dockerfile` and a `docker-compose.yml` file are included to aid in compiling
the desired version of Stockfish and to place the resulting binary in an
adjacent bin directory for use by the application.

#### Copyright and License
Copyright (C) 2023  Kris Lamoureux

This project is licensed under the 0BSD License - see the LICENSE file for
details.

