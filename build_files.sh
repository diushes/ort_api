pip install -r requirements.txt

python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrations --noinput

python3.9 manage.py collectstatic