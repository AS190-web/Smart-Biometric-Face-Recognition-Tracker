Automated Face Recognition Based Attendance System with Online Dashboard Tracking
📌 Overview
An intelligent, automated attendance management system that leverages advanced face recognition technology to mark attendance in real-time. The system features a comprehensive online dashboard for monitoring, tracking, and managing attendance records with visual analytics and reporting capabilities.

🚀 Key Features
🔍 Face Recognition & Detection
Real-time face detection using Haar Cascade Classifier

High-accuracy face recognition using LBPH (Local Binary Pattern Histogram) algorithm

Confidence-based recognition with adjustable threshold (default: 70)

Support for multiple user enrollment and recognition

😷 Mask Detection Integration
Dual-mode recognition for faces with and without masks

Synthetic dataset generation for mask-agnostic recognition

Real-time mask compliance monitoring

📊 Online Dashboard Tracking
Web-based dashboard for real-time attendance monitoring

Visual analytics and attendance reports

Date-wise attendance filtering and export capabilities

User management interface for adding/removing students

💾 Dual Storage System
CSV Storage: Local backup for offline operation

MySQL Database: Centralized storage for web dashboard

Real-time synchronization between local and cloud storage

🛡️ Smart Features
Duplicate entry prevention (one entry per person per day)

Confidence threshold filtering to eliminate false positives

Real-time video feed with bounding boxes and labels

Multi-user support with individual student IDs

┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Camera Input  │────▶│  Face Detection │────▶│  Recognition    │
│   (Webcam)      │     │  (Haar Cascade) │     │  (LBPH Model)   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Online        │◀────│  MySQL Database │◀────│  Attendance     │
│   Dashboard     │     │  (Central)      │     │  Marker         │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
                                              ┌─────────────────┐
                                              │  CSV Backup     │
                                              │  (Local Storage)│
                                              └─────────────────┘


