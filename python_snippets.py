# check if a variable name is illegal:
import keyword
keyword.iskeyword("keyword") # returns Boolean value


# check paths that Django is searching for a static file:
python manage.py findstatic --verbosity 2 <filepath>


# install package into specific non-default directory:
pip install --target=/my/directory/name/ <package>


# print elements of a list, one per line:
print(("\n").join(mylist))


# open and print contents of a file:
with open("my_file.txt") as my_file:
  my_file_contents = my_file.read()
print(my_file_contents)


# run a package if installed, but not on PATH:
python3 -m <package> <directory>


# get all reverse relations of a Django model,
# including type of relation:
[x for x in ModelName._meta.get.fields() if x.auto_created and not x.concrete]
