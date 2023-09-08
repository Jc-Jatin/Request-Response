# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 12:47:49 2023

@author: Jatin Chaudhary
"""

def get_custom_response(url):
    if url == "/home":
        return "Welcome home"
    elif url == "/about":
        return "Welcome to About Us page"
    elif url == "/node":
        return "Welcome to my Node Js project"
    else:
        return "Invalid URL"

# Example usage:
url = input("Enter the URL: ")
response = get_custom_response(url)
print(response)
