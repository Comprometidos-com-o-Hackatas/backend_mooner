set -o errexit
pip install --upgrade pip
pip install -r requirements.txt
python src/manage.py collectstatic --no-input
python src/manage.py migrate
