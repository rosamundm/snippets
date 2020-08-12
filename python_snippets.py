# check if a variable name is illegal:
import keyword
keyword.iskeyword("keyword") # returns Boolean value

# check paths that Django is searching for a static file:
python manage.py findstatic --verbosity 2 <filepath>
