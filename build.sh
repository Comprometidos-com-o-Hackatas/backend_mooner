set -o errexit
export DJANGO_SETTINGS_MODULE="src.config.settings"
export PYTHONPATH=$PYTHONPATH:/opt/render/project/src/backend_mooner/src
pip install --upgrade pip
pip install -r requirements.txt
python src/manage.py collectstatic --no-input
python src/manage.py migrate
