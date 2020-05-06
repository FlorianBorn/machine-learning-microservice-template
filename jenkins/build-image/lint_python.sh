# $1 ... a Path to a Python File (including it's filename)
pylint --exit-zero --extension-pkg-whitelist=pydantic $1 #--exit-zero returns always 0