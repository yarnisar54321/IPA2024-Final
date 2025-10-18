# ansible_final.py
import os
import subprocess


def showrun():
    # เรียก ansible-playbook ที่เตรียมไว้
    # ต้องมีไฟล์: ansible.cfg, hosts, playbook.yaml อยู่ในโฟลเดอร์โปรเจกต์
    cmd = ["ansible-playbook", "-i", "hosts", "playbook.yaml"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    out = result.stdout + "\n" + result.stderr

    # เช็คความสำเร็จแบบยืดหยุ่น: failed=0
    if "failed=0" in out.lower():
        return "ok"
    else:
        return "Error: Ansible"
