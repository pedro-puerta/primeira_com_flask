export FLASK_APP=app
export FLASK_ENV=development

python -m virtualenv venv
source venv/Scripts/activate
python -m pip install -r requirements.txt

python -m flask run --host=0.0.0.0