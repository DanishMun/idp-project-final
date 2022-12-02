# idp-project-final

--INSTALLATIONS (Requirements)--

1.To install virtual env:
python -m venv venv

2.Activate virutal env (from cmd):
venv\Scripts\activate

3. Update pip inside virtual env:
 python -m pip install --upgrade pip

4. To install requirements from requirements file
pip install -r requirements.txt

5. Create a project
django-admin.exe startproject Idpproject .

6.start app
python manage.py startapp hsi

7. To run app:

python manage.py runserver

(the application can be accessed as http://localhost:8000/home)

--HOW SOFTWARE WORKS----

1-run the server

2-add any tiff image into by going into folder directory Idp\hsi\static\images

3- open the admin panel of Database http://localhost:8000/admin

4- click on the binary image table and name of the of the tiff image that you have added in step-2 into the field called Filename:

5- access the application on http://localhost:8000/home 

6- click on any tiff image name on the right side 

7- software will generate all the png images and relevant data such as cube, wavelengths etc

8- data generated from tiff will be stored in the database
