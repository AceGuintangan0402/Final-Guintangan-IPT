1. Clone the Repository
First, clone the repository to your local development environment:


git clone https://github.com/AceGuintangan0402/Final-Guintangan-IPT.git


2. Create a Virtual Environment (Optional but Recommended)
Creating a virtual environment helps manage dependencies separately for each project:

python -m venv venv
Activate the virtual environment:

On Windows:

venv\Scripts\activate

3. Install Dependencies
Install the required Python packages using pip:

pip install -r requirements.txt

 
4. Update Configuration
Update the MySQL configuration in the app.py file with your MySQL credentials:

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "yourpassword"
app.config["MYSQL_DB"] = "cars"

5. Run the Application
Start the Flask application:


python app.py
The application will run in debug mode, and you can access it at http://localhost:5000.

6. Test the Endpoints
Use a tool like curl, Postman, or your web browser to test the endpoints. Ensure you include the Authorization header for secured endpoints.

Example using curl:

GET /cars:
curl -u user1:password1 -X GET "http://localhost:5000/cars?format=json"


POST /cars:
curl -u user1:password1 -X POST "http://localhost:5000/cars" -H "Content-Type: application/json" -d '{"model": "Model X", "year": 2022, "color": "Red", "manufacturer_id": 1}'


GET /cars/<id>:
curl -u user1:password1 -X GET "http://localhost:5000/cars/1?format=xml"


PUT /cars/<id>:
curl -u user1:password1 -X PUT "http://localhost:5000/cars/1" -H "Content-Type: application/json" -d '{"model": "Model Y", "year": 2023, "color": "Blue", "manufacturer_id": 2}'

DELETE /cars/<id>:
curl -u user1:password1 -X DELETE "http://localhost:5000/cars/1"

Following these steps will set up the ACE Database API on your local development environment, allowing you to manage car records securely and efficiently.
