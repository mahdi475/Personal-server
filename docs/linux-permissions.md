# Linux File Permissions

This document records a practical Linux permissions test performed on the
Personal Server.

## Users and Groups

The main Linux user is:

- `mahdi`

A development group was created:

- `developers`

The user `mahdi` was added to the `developers` group.

A separate test user was created:

- `tester`

The `tester` user was intentionally not added to the `developers` group.

## File Ownership

A test file was created:

```text
project.txt

Its ownership was changed to:

mahdi:developers

The resulting permissions were:

-rw-rw-r-- 1 mahdi developers project.txt

This means:

Permission	Meaning
rw-	Owner can read and write
rw-	Group can read and write
r--	Others can only read
Verification

The tester user was used to test the permissions.

Command:

sudo -u tester bash

Then:

echo "tester was here" >> project.txt

Result:

bash: project.txt: Permission denied

This confirms that a user who is not a member of the developers group cannot
write to the file.

What This Demonstrates

The test demonstrates Linux's three basic permission categories:

owner
group
others

and shows how file ownership and group membership affect access to files.



### Sedan


1. **Ctrl + S**
2. Gå till terminalen i VS Code.
3. Kör:


```bash
git status