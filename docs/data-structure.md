# Data Structure

## Project Title
IceCream

## 1. Main Data Entities / Tables
Example entities: Users, Reports, Bookings, Items, Requests, Tasks, Products, Appointments, Feedback.

| Entity / Table | Purpose                                       | Example Records |
|----------------|-----------------------------------------------|---|
| Users          | Basic entity for all users                    | |
| Artworks       | To store artwork file address and information | |
| Comments       | To store Comments                             | |

## 2. Field Definition

| Entity   | Field Name   | Data Type     | Required? | Example Value                     | Validation Rule | Used For Search/Filter? |
|----------|--------------|---------------|-----------|-----------------------------------|-----------------|-------------------------|
| Users    | User_id      | Text/ID       | Yes       | U001                              | Unique value    | Yes                     |
| Users    | Nickname     | Text          | Yes       | Jack                              | Unique value    | Yes                     |
| Users    | Password     | Text          | Yes       | *******                           | No              | No                      |
| Artworks | Art_id       | Text/ID       | Yes       | A001                              | Unique value    | Yes                     |    
| Artworks | User_id      | Text/ID       | Yes       | U001                              | Unique Value    | Yes                     |
| Artworks | Title        | Text          | Yes       | Sunset Study                      | 1–100 characters | Yes                    |
| Artworks | Description  | Text          | No        | Digital color study               | Up to 2,000 characters | No               |
| Artworks | Image_URLs   | JSON/List     | Yes       | `["/uploads/a006-1.png"]`         | 1–5 valid image paths | No                  |
| Artworks | Tags         | Tag/List      | Yes       | `digital\|sunset`                 | 1–10 tags       | Yes                     |
| Artworks | View_Count   | Integer       | Yes       | 0                                 | Zero or higher  | No                      |
| Artworks | Like_Count   | Integer       | Yes       | 0                                 | Zero or higher  | No                      |
| Artworks | Comment_Count | Integer      | Yes       | 0                                 | Zero or higher  | No                      |
| Artworks | Sanity_Level | Integer       | Yes       | 0                                 | 0, 18, or 19    | Yes                     |
| Artworks | Status       | Text          | Yes       | Underchecking/Published/Withdrawn | Allowed status value | Yes                |
| Artworks | Created_At   | DateTime      | Yes       | 2026-07-26T09:00:00+00:00         | UTC timestamp   | No                      |
| Artworks | Updated_At   | DateTime      | Yes       | 2026-07-26T09:00:00+00:00         | UTC timestamp   | No                      |
| Artworks | Deleted_At   | DateTime      | No        |                                   | UTC timestamp when deleted | No              |
| Comments | Comments_id  | Text/ID       | Yes       | C001                              | Unique Value    | Yes                     |
| Comments | Art_id       | Text/ID       | Yes       | A001                              | Unique Value    | Yes                     |
| Comments | User_id      | Text/ID       | Yes       | U001                              | Unique Value    | Yes                     |
| Comments | Content      | Text          | Yes       | Hellow_world                      | No              | Yes                     |
| Artworks | Status       | Text          | Yes       | Underchecking/Published/Withdrawn | Unique Value    | Yes                     |

## 3. Status Values
Define the status values used in the prototype.

| Status        | Meaning                                                      | Who Can Update? |
|---------------|--------------------------------------------------------------|-----------------|
| Underchecking | artworks or comments are temporaryly taken down              | Admin           |
| Published     | artworks or comments are sucessfully published               | normal users    |
| Withdrawn     | artworks or comments are removed by the publisher themselves | normal users    |

## 4. Sample Records
Sample mock records are available in:

- `/data/mock-users.csv`
- `/data/mock-artworks.csv`
- `/data/mock-comments.csv`

## 5. Data Privacy Note
Explain what sensitive data will not be collected and how sample data will be anonymized.

Because user passwords are considered private information and are not relevant to user behavior analysis, we do not collect user passwords.
