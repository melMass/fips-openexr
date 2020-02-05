"""verb import install_boost"""

from mod import log
import subprocess
import platform
#-------------------------------------------------------------------------------
def run(proj_dir, fips_dir, args) :
    print(proj_dir)
    print(fips_dir)
    print(args)
    log.info(platform.system())
    if platform.system() == "Darwin":
      log.info(log.YELLOW + 
              "Updating & running Brew to install Boost\n"
              + log.DEF +
            "    boost boost-python & boost-python3.")
      subprocess.call(["brew", "update"])
      subprocess.call(["brew", "install", "boost"])
      subprocess.call(["brew", "install", "boost-python"])
      subprocess.call(["brew", "install", "boost-python3"])

      
#-------------------------------------------------------------------------------
def help() :
    log.info(log.YELLOW +
            "./fips install_boost\n"
            + log.DEF +
            "    Install boost libraries system wide.")


