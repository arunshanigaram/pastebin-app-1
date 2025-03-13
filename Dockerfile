# Use a lightweight Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run the application
CMD ["hypercorn", "app.main:asgi_app", "--bind", "0.0.0.0:8000"]
