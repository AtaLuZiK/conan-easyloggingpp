import os

from conans import ConanFile, CMake, tools


class EasyloggingConan(ConanFile):
    name = "easyloggingpp"
    version = "9.96.5"
    license = "MIT"
    url = "https://github.com/AtaLuZiK/conan-easyloggingpp"
    description = "Feature-rich single header C++ logging library"
    settings = "os", "compiler", "build_type", "arch"
    options = {"utc_datetime": [True, False]}
    default_options = "utc_datetime=False"
    exports_sources = "easyloggingpp-config.cmake"
    generators = "cmake"

    @property
    def zip_folder_name(self):
        return "easyloggingpp-%s" % self.version

    def source(self):
        zip_name = "v%s.tar.gz" % self.version
        tools.download("https://github.com/muflihun/easyloggingpp/archive/%s" % zip_name, zip_name)
        tools.check_md5(zip_name, "f9a18180fa0842e8744749a4fe3e3ce9")
        tools.unzip(zip_name)
        os.unlink(zip_name)

        with tools.chdir(self.zip_folder_name):
            tools.replace_in_file("CMakeLists.txt", "project(Easyloggingpp CXX)", '''project(Easyloggingpp CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')
            tools.replace_in_file("CMakeLists.txt", "add_library(easyloggingpp STATIC src/easylogging++.cc)", '''add_library(easyloggingpp STATIC src/easylogging++.cc)
add_definitions(-DELPP_NO_DEFAULT_LOG_FILE)''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["build_static_lib"] = "ON"
        cmake.definitions["lib_utc_datetime"] = "ON" if self.options.utc_datetime else "OFF"
        cmake.configure(source_folder=self.zip_folder_name)
        cmake.build()

    def package(self):
        self.copy("easylogging++.h", dst="include", src=os.path.join(self.zip_folder_name, "src"))
        self.copy("easyloggingpp.lib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("easyloggingpp-config.cmake", "cmake", ".")

    def package_info(self):
        self.cpp_info.libs = ["easyloggingpp"]

