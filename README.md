# smart-class-attendence-system
Overview

This project implements a real-time Smart Class Attendance System using Python and OpenCV. The system captures student attendance and stores it in a database.

Features

- Real-time attendance tracking
- Face detection and recognition using OpenCV
- Attendance data stored in a database (e.g., MySQL, SQLite)
- User-friendly GUI interface

Requirements

- Python 3.x
- OpenCV 4.x
- Database management system (e.g., MySQL, SQLite)
- Tkinter or other GUI library

Usage

1. Launch the application.
2. Select the class and lecture.
3. The system will start capturing attendance.
4. Students' faces will be detected and recognized.
5. Attendance data will be stored in the database.

Database Schema

The database schema consists of the following tables:

- students: stores student information (id, name, roll number, etc.)
- attendance: stores attendance records (id, student_id, date, time, etc.)

