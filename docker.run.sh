sudo rm -f ./build/html/*.html

docker run --rm -v $PWD:/docs sphinxdoc/sphinx:v3 make html



 http-server ./build/html/ -p 8888
 
