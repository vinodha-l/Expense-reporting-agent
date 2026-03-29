# 1. Use Python as the base
FROM python:3.10-slim

# 2. Create a folder inside the 'box' for our code
WORKDIR /app

# 3. Install the tools listed in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy ALL your files (env.py, models.py, etc.) into the box
COPY . .

# 5. Tell Hugging Face to use Port 7860 (The 'Door' for the Space)
EXPOSE 7860

# 6. Start the script! 
# We run inference.py because it's the 'Brain' that talks to the 'Office'
CMD ["python", "inference.py"]
