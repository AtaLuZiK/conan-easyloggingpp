find_path(EASYLOGGINGPP_INCLUDE_PDIR NAMES easylogging++.h PATHS ${CONAN_INCLUDE_DIRS_EASYLOGGINGPP})
find_library(EASYLOGGINGPP_LIBRARY NAMES easylogging PATHS ${CONAN_LIB_DIRS_EASYLOGGINGPP})

add_library(easyloggingpp INTERFACE IMPORTED)
target_include_directories(easyloggingpp INTERFACE ${EASYLOGGINGPP_INCLUDE_PDIR})
target_link_libraries(easyloggingpp INTERFACE ${EASYLOGGINGPP_LIBRARY})

mark_as_advanced(EASYLOGGINGPP_INCLUDE_PDIR EASYLOGGINGPP_LIBRARY)

message("** Easylogging++ found by Conan!")
set(EASYLOGGINGPP_FOUND TRUE)
message("   - includes: ${EASYLOGGINGPP_INCLUDE_PDIR}")
message("   - libraries: ${EASYLOGGINGPP_LIBRARY}")
