# Step 1: Base image with Python environment
FROM python:3.12-slim AS base

# Step 2: Set working directory
WORKDIR /app

# Step 3: Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the project files into the container
COPY . .

# Step 5: Define the entry point
ENTRYPOINT ["python", "/app/travel_planning_agent.py"]
