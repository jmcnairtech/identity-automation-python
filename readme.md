# identity-automation-python

A modular Python toolkit for automating identity and endpoint workflows using Microsoft Graph.  
This project supports real-world identity engineering tasks aligned with SC-300 and MD-102, including user and group automation, reporting, and future Intune device workflows.

## Project Overview

This repository provides a clean, extensible foundation for building automation scripts that interact with Microsoft Graph.  
It includes:

- Reusable authentication module (MSAL)
- User and group export scripts
- CSV export utilities
- A structure designed for future expansion (Intune, Conditional Access, Governance)

## Folder Structure

identity-automation-python/
│
├── requirements.txt        # Python dependencies
│
├── auth/                   # Authentication logic
│   └── graph_auth.py
│
├── users/                  # User automation scripts
│   └── list_users.py
│
├── groups/                 # Group automation scripts
│   └── list_groups.py
│
└── utils/                  # Helper utilities
    └── csv_writer.py

## Authentication Setup

This project uses MSAL (Microsoft Authentication Library) with OAuth2 client credentials.

You will need:

- Tenant ID
- Client ID
- Client Secret
- A registered app in Entra ID with Microsoft Graph permissions

Create a `.env` file in your local environment:

TENANT_ID=your-tenant-id
CLIENT_ID=your-client-id
CLIENT_SECRET=your-client-secret

Do not commit your `.env` file to GitHub.

## Installation

Install dependencies:

pip install -r requirements.txt

## Running Scripts

List all Entra ID users:

python users/list_users.py

Exports: users.csv

List all Entra ID groups:

python groups/list_groups.py

Exports: groups.csv

## Roadmap

Planned modules include:

- Intune device inventory automation (MD-102)
- Conditional Access policy exporter (SC-300)
- External user audit tool (guest access governance)
- Authentication strength reporting
- Autopilot device queries

## License

MIT License
