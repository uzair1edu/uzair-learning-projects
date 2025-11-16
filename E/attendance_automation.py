# attendance_automation.py
# Demo: mark attendance from a simple list

members = ["Uzair","Aisha","Bilal","Sara"]
present = ["Uzair","Sara"]

attendance = {m: ("Present" if m in present else "Absent") for m in members}
for k,v in attendance.items():
    print(k, v)
