# Dropzone Action Info
# Name: SHA-256 Checksum
# Description: check the sha-256 sum
# Handles: Files
# Creator: rhysbw
# URL: http://yoursite.com
# Events: Dragged
# KeyModifiers: Command, Option, Control, Shift
# SkipConfig: No
# RunsSandboxed: Yes
# Version: 1.0
# MinDropzoneVersion: 3.5


"""
You must have notifications for it to work
"""
import time
import hashlib

def dragged():
    

    # Below line switches the progress display to determinate mode so we can show progress
    dz.determinate(False)
    
    

    
    correct_hash = get_needed_sha256_hash()
    
    found_hash = calc_sha256_hash()
    
    
    if (correct_hash == found_hash):
    
        dz.finish(f"sha256_hash Sum Valid, Hash calculated: {found_hash}")
        dz.url(False)
        
    
    
    else:
        dz.finish(f"Invalid sha256_hash, Hash calculated: {found_hash}")
        dz.url(False)



def get_needed_sha256_hash():
    sha256 = dz.inputbox("SHA256", "Enter SHA256 hash:")
    return sha256
    
def calc_sha256_hash():
    sha256_hash = hashlib.sha256()
    with open(items[0], "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
    return sha256_hash.hexdigest()
