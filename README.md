# conan-easyloggingpp

Conan package for [Easylogging++](https://github.com/muflihun/easyloggingpp)

The packages generated with this **conanfile** can be found on [bintray](https://bintray.com/conan-community).

## Package Status

| Bintray | Travis | Appveyor |
|---------|--------|----------|
|[ ![Download](https://api.bintray.com/packages/zimmerk/conan/easyloggingpp%3Azimmerk/images/download.svg) ](https://bintray.com/zimmerk/conan/easyloggingpp%3Azimmerk/_latestVersion)|[![Build Status](https://travis-ci.org/AtaLuZiK/conan-easyloggingpp.svg?branch=release%2F9.96.5)](https://travis-ci.org/AtaLuZiK/conan-easyloggingpp)|[![Build status](https://ci.appveyor.com/api/projects/status/to3nbc3pql44txax/branch/release/9.96.5?svg=true)](https://ci.appveyor.com/project/AtaLuZiK/conan-easyloggingpp/branch/release/9.96.5)|

## Reuse the packages

### Basic setup

```
conan install easyloggingpp/9.96.5@zimmerk/stable
```

### Project setup

```
[requires]
easyloggingpp/9.96.5@zimmerk/stable

[options]
# Take a look for all avaliable options in conanfile.py

[generators]
cmake
```

Complete the installitation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files conanbuildinfo.txt and conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io
