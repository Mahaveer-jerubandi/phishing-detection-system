# 📖 User Manual: Real-Time Phishing Detection System

This manual provides instructions for using and deploying the **Real-Time Phishing Detection System**.

---

## 🧭 Table of Contents

1. [Introduction](#1-introduction)
2. [System Requirements](#2-system-requirements)
3. [Installation Guide](#3-installation-guide)
4. [How to Use the Web Interface](#4-how-to-use-the-web-interface)
5. [Running the System on AWS](#5-running-the-system-on-aws)
6. [Troubleshooting](#6-troubleshooting)
7. [Contact & Support](#7-contact--support)

---

## 1. Introduction

The **Real-Time Phishing Detection System** is designed to protect users from phishing attacks by analyzing:
- 📧 **Email content** for suspicious language
- 🔗 **URLs** for malicious patterns

It uses **machine learning** and **NLP** to provide instant feedback with risk scores and recommendations.

---

## 2. System Requirements

### Local Development
- **OS**: Windows, macOS, or Linux
- **Python**: 3.8 or higher
- **RAM**: 8 GB minimum (16 GB recommended)
- **Storage**: 500 MB free space

### Cloud Deployment (AWS)
- **Instance Type**: `t2.micro` (Free Tier eligible)
- **Security Group**: Open ports 22 (SSH), 80 (HTTP), 5000 (Flask)
- **Key Pair**: `.pem` file for SSH access

---

## 3. Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/real-time-phishing-detection.git
cd real-time-phishing-detection