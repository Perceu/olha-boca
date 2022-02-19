
cp ./contrib/env-sample .env

echo -e "\nSECRET_KEY=$(python3 ./contrib/secretkey.py)" >> .env

make