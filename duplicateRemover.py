# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:10:53 2024

@author: user
"""

import os
import hashlib
from tqdm import tqdm

def find_duplicates(directory):
  duplicates = {}
 
  for root, _, files in os.walk(directory):
    for filename in tqdm(files, desc=f"Processing {root}"):
      filepath = os.path.join(root, filename)
      
      try:
        with open(filepath, 'rb') as f:
          hasher = hashlib.sha256()
          while True:
            chunk = f.read(4096)
            if not chunk:
              break
            hasher.update(chunk)
          file_hash = hasher.hexdigest()
          
          if file_hash in duplicates:
            duplicates[file_hash].append(filepath)
          
          else:
            duplicates[file_hash] = [filepath]
      
        
      except Exception as e:
        print(f"Error processing {filepath}: {e}")
  
    return duplicates

def remove_duplicates(duplicates):
 
  for file_hash, filepaths in duplicates.items():
   
      if len(filepaths) > 1:
      # Keep the first file, delete the rest
      keep_file = filepaths[0]
     
      for duplicate_file in filepaths[1:]:
        
          try:
          os.remove(duplicate_file)
          print(f"Removed duplicate: {duplicate_file}")
          
          except Exception as e:
          print(f"Error removing {duplicate_file}: {e}")

directory_to_scan = "/path/to/your/directory"
remove_duplicates(find_duplicates(directory_to_scan))