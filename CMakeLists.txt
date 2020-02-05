#
# project: fips-openexr
#

if (NOT FIPS_IMPORT)
    cmake_minimum_required(VERSION 2.8)
    get_filename_component(FIPS_ROOT_DIR "../fips" ABSOLUTE)
    include("${FIPS_ROOT_DIR}/cmake/fips.cmake")
    fips_setup()
    fips_project(openexr)
endif()

fips_project(openexr)
set(ILMBASE_BUILD_SHARED OFF CACHE BOOL " " FORCE)
set(OPENEXR_BUILD_SHARED OFF CACHE BOOL " " FORCE)
set(ILMBASE_BUILD_STATIC ON CACHE BOOL " " FORCE)
set(OPENEXR_BUILD_STATIC ON CACHE BOOL " " FORCE)
set(PYILMBASE_ENABLE OFF CACHE BOOL " " FORCE)
set(OPENEXR_VIEWERS_ENABLE OFF CACHE BOOL " " FORCE)
set(ILMBASE_NAMESPACE_VERSIONING OFF CACHE BOOL " " FORCE)
set(OPENEXR_NAMESPACE_VERSIONING OFF CACHE BOOL " " FORCE)
set(OPENEXR_INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}/openexr CACHE PATH " " FORCE)

fips_add_subdirectory(openexr EXCLUDE_FROM_ALL)

target_compile_options(IexMath PUBLIC -fexceptions -frtti) 
target_compile_options(IlmThread PUBLIC -fexceptions -frtti) 
target_compile_options(Half PUBLIC -fexceptions -frtti) 
target_compile_options(Iex PUBLIC -fexceptions -frtti) 
target_compile_options(Imath PUBLIC -fexceptions -frtti) 
target_compile_options(IlmImf PUBLIC -fexceptions -frtti)


set_property(TARGET IexMath IlmThread Half Iex Imath IlmImf PROPERTY FOLDER "Dependencies")

include_directories(${OPENEXR_INCLUDE_DIRS})
add_definitions(-DUSE_OPENEXR)

if (NOT FIPS_IMPORT)
    fips_finish()
endif()