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

# disable shared libraries
set(ILMBASE_BUILD_SHARED OFF CACHE BOOL " " FORCE)
set(OPENEXR_BUILD_SHARED OFF CACHE BOOL " " FORCE)

# enable static..
set(ILMBASE_BUILD_STATIC ON CACHE BOOL " " FORCE)
set(OPENEXR_BUILD_STATIC ON CACHE BOOL " " FORCE)

# disable python ILMBase & EXR Viewers
set(PYILMBASE_ENABLE OFF CACHE BOOL " " FORCE)
set(OPENEXR_VIEWERS_ENABLE OFF CACHE BOOL " " FORCE)

# remove versionning from namespaces
set(ILMBASE_NAMESPACE_VERSIONING OFF CACHE BOOL " " FORCE)
set(OPENEXR_NAMESPACE_VERSIONING OFF CACHE BOOL " " FORCE)

set(OPENEXR_INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}/openexr CACHE PATH " " FORCE)

set(CMAKE_THREAD_PREFER_PTHREAD TRUE)
set(THREADS_PREFER_PTHREAD_FLAG TRUE)
find_package(Threads)
if(NOT Threads_FOUND)
  message(FATAL_ERROR "Unable to find a threading library which is required for IlmThread")
endif()

ilm_version()

fips_add_subdirectory(openexr/IlmBase/config)

# Half
fips_begin_lib(Half)
    fips_dir(openexr/IlmBase/Half)
    fips_files(
        toFloat.h
        eLut.h
        half.cpp
        half.h
        halfFunction.h
        halfExport.h
        halfLimits.h
    )
   fips_include_directories(openexr/IlmBase/Half)
fips_end_lib()
# Iex
fips_begin_lib(Iex)
    fips_dir(openexr/IlmBase/Iex)
    fips_files(
        IexBaseExc.cpp
        IexThrowErrnoExc.cpp
        IexBaseExc.h
        IexMathExc.h
        IexThrowErrnoExc.h
        IexErrnoExc.h
        IexMacros.h
        Iex.h
        IexNamespace.h
        IexExport.h
        IexForward.h
    )
   fips_include_directories(openexr/IlmBase/Iex)
   fips_deps(IlmBase::Config)
fips_end_lib()

# IexMath
fips_begin_lib(IexMath)
    fips_dir(openexr/IlmBase/IexMath)
    fips_files(
        IexMathFloatExc.cpp
        IexMathFpu.cpp
        IexMathFloatExc.h
        IexMathFpu.h
        IexMathIeeeExc.h
    )
    fips_deps(Iex)
   fips_include_directories(openexr/IlmBase/IexMath)

fips_end_lib()

# Imath
fips_begin_lib(Imath)
    fips_dir(openexr/IlmBase/Imath)
    fips_files(
        ImathRandom.cpp
        ImathColorAlgo.cpp
        ImathFun.cpp
        ImathVec.cpp
        ImathExc.cpp
        ImathMatrixAlgo.cpp
        ImathBoxAlgo.h
        ImathBox.h
        ImathColorAlgo.h
        ImathColor.h
        ImathEuler.h
        ImathExc.h
        ImathExport.h
        ImathForward.h
        ImathFrame.h
        ImathFrustum.h
        ImathFrustumTest.h
        ImathFun.h
        ImathGL.h
        ImathGLU.h
        ImathHalfLimits.h
        ImathInt64.h
        ImathInterval.h
        ImathLimits.h
        ImathLineAlgo.h
        ImathLine.h
        ImathMath.h
        ImathMatrixAlgo.h
        ImathMatrix.h
        ImathNamespace.h
        ImathPlane.h
        ImathPlatform.h
        ImathQuat.h
        ImathRandom.h
        ImathRoots.h
        ImathShear.h
        ImathSphere.h
        ImathVecAlgo.h
        ImathVec.h
    )
    fips_deps(IexMath Half)
   fips_include_directories(openexr/IlmBase/Imath)

fips_end_lib()
  
# IlmThread
fips_begin_lib(IlmThread)
    fips_dir(openexr/IlmBase/IlmThread)
    fips_files(
        IlmThread.cpp
        IlmThreadMutex.cpp
        IlmThreadMutexPosix.cpp
        IlmThreadPool.cpp
        IlmThreadPosix.cpp
        IlmThreadSemaphore.cpp
        IlmThreadSemaphorePosixCompat.cpp
        IlmThreadSemaphorePosix.cpp
        IlmThreadSemaphoreOSX.cpp
        IlmThreadMutexWin32.cpp
        IlmThreadSemaphoreWin32.cpp
        IlmThreadWin32.cpp
    )
    fips_deps(Iex Threads::Threads)
    fips_include_directories(openexr/IlmBase/IlmThread)
fips_end_lib()

fips_add_subdirectory(openexr/OpenEXR/config)

fips_begin_lib(IlmImf)
    fips_dir(openexr/OpenEXR/IlmImf)
    fips_files(
        b44ExpLogTable.h
        dwaLookups.h
        ImfAttribute.cpp
        ImfBoxAttribute.cpp
        ImfCRgbaFile.cpp
        ImfChannelList.cpp
        ImfChannelListAttribute.cpp
        ImfFloatAttribute.cpp
        ImfFrameBuffer.cpp
        ImfHeader.cpp
        ImfIO.cpp
        ImfInputFile.cpp
        ImfIntAttribute.cpp
        ImfLineOrderAttribute.cpp
        ImfMatrixAttribute.cpp
        ImfOpaqueAttribute.cpp
        ImfOutputFile.cpp
        ImfRgbaFile.cpp
        ImfStringAttribute.cpp
        ImfVecAttribute.cpp
        ImfHuf.cpp
        ImfThreading.cpp
        ImfWav.cpp
        ImfLut.cpp
        ImfCompressor.cpp
        ImfRleCompressor.cpp
        ImfZipCompressor.cpp
        ImfPizCompressor.cpp
        ImfB44Compressor.cpp
        ImfDwaCompressor.cpp
        ImfMisc.cpp
        ImfCompressionAttribute.cpp
        ImfDoubleAttribute.cpp
        ImfConvert.cpp
        ImfPreviewImage.cpp
        ImfPreviewImageAttribute.cpp
        ImfVersion.cpp
        ImfChromaticities.cpp
        ImfChromaticitiesAttribute.cpp
        ImfKeyCode.cpp
        ImfKeyCodeAttribute.cpp
        ImfTimeCode.cpp
        ImfTimeCodeAttribute.cpp
        ImfRational.cpp
        ImfRationalAttribute.cpp
        ImfFramesPerSecond.cpp
        ImfStandardAttributes.cpp
        ImfStdIO.cpp
        ImfEnvmap.cpp
        ImfEnvmapAttribute.cpp
        ImfScanLineInputFile.cpp
        ImfTiledInputFile.cpp
        ImfTiledMisc.cpp
        ImfTiledOutputFile.cpp
        ImfTiledRgbaFile.cpp
        ImfTileDescriptionAttribute.cpp
        ImfTileOffsets.cpp
        ImfRgbaYca.cpp
        ImfPxr24Compressor.cpp
        ImfTestFile.cpp
        ImfStringVectorAttribute.cpp
        ImfMultiView.cpp
        ImfAcesFile.cpp
        ImfMultiPartOutputFile.cpp
        ImfGenericOutputFile.cpp
        ImfOutputPartData.cpp
        ImfMultiPartInputFile.cpp
        ImfGenericInputFile.cpp
        ImfPartType.cpp
        ImfInputPartData.cpp
        ImfOutputPart.cpp
        ImfTiledOutputPart.cpp
        ImfInputPart.cpp
        ImfTiledInputPart.cpp
        ImfDeepScanLineInputPart.cpp
        ImfDeepScanLineOutputPart.cpp
        ImfDeepScanLineInputFile.cpp
        ImfDeepScanLineOutputFile.cpp
        ImfDeepTiledInputPart.cpp
        ImfDeepTiledOutputPart.cpp
        ImfDeepTiledInputFile.cpp
        ImfDeepTiledOutputFile.cpp
        ImfDeepFrameBuffer.cpp
        ImfDeepCompositing.cpp
        ImfCompositeDeepScanLine.cpp
        ImfDeepImageStateAttribute.cpp
        ImfFastHuf.cpp
        ImfFloatVectorAttribute.cpp
        ImfRle.cpp
        ImfSystemSpecific.cpp
        ImfZip.cpp
    )
    fips_deps(OpenEXR::Config Iex Half Imath IlmThread ZLIB::ZLIB)
    fips_include_directories(openexr/OpenEXR/IlmImf)
fips_end_lib()

fips_begin_lib(IlmImfUtil)
    fips_dir(openexr/OpenEXR/IlmImfUtil)
    fips_files(
        ImfImageChannel.cpp
        ImfFlatImageChannel.cpp
        ImfDeepImageChannel.cpp
        ImfSampleCountChannel.cpp
        ImfImageLevel.cpp
        ImfFlatImageLevel.cpp
        ImfDeepImageLevel.cpp
        ImfImage.cpp
        ImfFlatImage.cpp
        ImfDeepImage.cpp
        ImfImageIO.cpp
        ImfFlatImageIO.cpp
        ImfDeepImageIO.cpp
        ImfImageDataWindow.cpp
    )
    fips_deps(IlmImf)
    fips_include_directories(openexr/OpenEXR/IlmImfUtil)
fips_end_lib()

# fips_add_subdirectory(openexr EXCLUDE_FROM_ALL)

# maybe mac specific, I have to check
# target_compile_options(IexMath PUBLIC -fexceptions -frtti) 
# target_compile_options(IlmThread PUBLIC -fexceptions -frtti) 
target_compile_options(Half PUBLIC -fexceptions -frtti) 
target_compile_options(Iex PUBLIC -fexceptions -frtti) 
# target_compile_options(Imath PUBLIC -fexceptions -frtti) 
# target_compile_options(IlmImf PUBLIC -fexceptions -frtti)


# set_property(TARGET IexMath IlmThread Half Iex Imath IlmImf PROPERTY FOLDER "Dependencies")

#include_directories(${OPENEXR_INCLUDE_DIRS})
#add_definitions(-DUSE_OPENEXR)

if (NOT FIPS_IMPORT)
    fips_finish()
endif()