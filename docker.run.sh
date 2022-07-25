rm -f ./build/html/*.html

docker run --rm -v $PWD:/docs sphinxdoc/sphinx:v3 make html



