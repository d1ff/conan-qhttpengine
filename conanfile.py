from conans import ConanFile, CMake, tools


class QhttpengineConan(ConanFile):
    name = "qhttpengine"
    version = "0.1.0"
    license = "LGPL"
    author = "Vladislav Bortnikov facepalmlite@gmail.com"
    url = "https://github.com/d1ff/quazip-qhttpwebengine"
    description = "Simple set of classes for developing HTTP server applications in Qt."
    topics = ("http",)
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake"
    requires = ("qt/5.14.2@d1ff/stable",)

    def source(self):
        self.run("git clone --branch 0.1.0 https://github.com/nitroshare/qhttpengine.git")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("qhttpengine/CMakeLists.txt", "project(QHttpEngine)",
                              '''project(QHttpEngine)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        
        cmake.configure(source_folder="qhttpengine")
        cmake.build()
        
    def package(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure(source_folder="qhttpengine")
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["qhttpengine"]

