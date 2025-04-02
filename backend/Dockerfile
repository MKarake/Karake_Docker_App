# Use official Python image 
#This tells Docker to start from an official Python image that has Python 3.9 installed.
#The slim version is smaller and faster to build.
#Always start with FROM because Docker builds from the base image upward, step by step.
FROM python:3.9-slim
 
#This tells Docker: "From now on, run everything inside the /app folder."
#WORKDIR must come before any file operations (COPY), otherwise files might be placed in the wrong directory
#So any files copied, commands run, etc., happen in this folder.
WORKDIR /app 

#This copies only the requirements.txt file into the container (into /app).
#This is done early so that if your code changes, Docker won’t reinstall the libraries again — it will reuse the cache.
COPY ../requirements.txt ./

#This command installs all Python dependencies listed in requirements.txt.
#--no-cache-dir means "don’t save temp files" — it keeps the image smaller
RUN pip install --no-cache-dir -r requirements.txt


#This copies all your backend code into the container’s /app folder.
#This comes after installing dependencies so the build doesn't reinstall libraries every time you change your code.

COPY . .

#specify the port on which the backend will 
#This container listens on port 8000
EXPOSE 8000


# Runs the Uvicorn Server installed from req.txt
# CMD This tells Docker: “This is the default command to run when the container starts.”
#"uvicorn"	This is the ASGI server that runs your FastAPI app. You installed it in requirements.txt.
#"app:app" First app = filename app.py (in the root) ;   Second app = FastAPI instance inside app.py (app = FastAPI())
#Tells Uvicorn where to find the FastAPI app ;  
#--host 0.0.0.0 makes the API accessible from outside (via http://localhost:8000/)
#Matches the port exposed in the Dockerfile 8000 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
