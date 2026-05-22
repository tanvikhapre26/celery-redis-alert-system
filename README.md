# Celery + Redis Alert System

A simple asynchronous alert processing system using **Celery** and **Redis**.

This project demonstrates how sensor data can be processed in the background using distributed task queues.

## 🚀 Tech Stack
- Python
- Celery
- Redis

## 📂 Project Structure
- `producer.py` – Sends alert tasks
- `task.py` – Celery worker that processes alerts
- `requirements.txt` – Project dependencies

## ⚙️ Prerequisites
- Python 3.x
- Redis installed and running

## 🔧 Installation

```bash
pip install -r requirements.txt
