cmake_minimum_required(VERSION 3.10)
project(bitcoin-utils)

set(CMAKE_CXX_STANDARD 11)

add_library(bitcoin-utils vanity-miner.cpp library.cpp library.h)
#add_executable(bitcoin-utils vanity-miner.cpp)