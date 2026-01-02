# 1. Use Python
FROM python:3.10-slim

# 2. Setup the folder
WORKDIR /app

# 3. Install Ingredients (Libraries)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the code
COPY . /app/

# 5. Open the door (Port)
EXPOSE 8000

# 6. The Start Command (Run migrations -> Start Server)
# We use this chain so the database sets itself up automatically on the cloud.
CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"