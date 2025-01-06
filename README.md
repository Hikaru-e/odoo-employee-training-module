# Employee Training Management Module for Odoo

A comprehensive Odoo module for managing employee training sessions, topics, and attendance tracking.

## Features

- **Training Topics Management**
  - Create and manage training subjects
  - Add detailed descriptions for each topic

- **Training Sessions**
  - Schedule training sessions with start/end dates
  - Assign instructors
  - Set seat limits
  - Track session states (Draft → Open → Done)
  - Monitor attendance rates

- **Attendance Management**
  - Enroll employees in sessions
  - Track check-ins
  - Prevent overbooking with seat limits

- **Reports**
  - Generate detailed session reports
  - View attendance statistics
  - Track training completion rates

## Installation

1. Clone this repository into your Odoo addons directory:
```bash
git clone https://github.com/Hikaru-e/odoo-employee-training-module.git
```

2. Update your Odoo modules list:
    
    - Go to Apps
    - Click "Update Apps List"
3. Search for "Employee Training Management" and install the module
    

## Configuration

1. Assign users to the "Training Manager" group for full access
2. Regular employees will have read-only access to training information

## Usage

### Creating Training Topics

1. Navigate to Training → Topics
2. Click "Create" to add new training topics
3. Fill in topic name and description

### Managing Training Sessions

1. Go to Training → Sessions
2. Create new sessions by selecting:
    - Topic
    - Instructor
    - Date/Time
    - Seat limit
3. Use state buttons to manage session progression

### Enrolling Employees

1. Open a training session in draft state
2. Click "Enroll Employees" action
3. Select employees from the wizard
4. Confirm enrollment

## Dependencies

- HR module (`hr`)
- Mail module (`mail`)
- Base Odoo (`base`)

## Security

The module implements three levels of access:

- Training Managers: Full access
- Regular Users: Limited read/write access
- Employees: Basic read access

## License

This module is licensed under LGPL-3.

## Contributors

- [EL AKHIRI OUSSAMA](https://github.com/Hikaru-e)
- [LAMCHANNEQ ZAKARIA](https://github.com/ZakariaLamchanneq)


## Video Demonstration

A video demonstrating the utilization of the module is available below:

[![Video Demonstration](https://img.youtube.com/vi/1UQkZjotrhUrkO_9cUYMIyM9YtuKbsd0W/0.jpg)](https://drive.google.com/file/d/1UQkZjotrhUrkO_9cUYMIyM9YtuKbsd0W/view?usp=sharing)


## Support

For issues and feature requests, please use the GitHub issues tracker.