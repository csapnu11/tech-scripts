To create a new user `bbb` with UID `1000`, while retaining the existing user `aaa` (who is a sudoer), follow these steps:

1. **Create the new user `bbb` with UID 1000**:
   You will need to create the new user while explicitly setting the UID to 1000. This is done with the `useradd` command, and since UID 1000 is already taken by `aaa`, you should be careful with this:

   ```
   sudo useradd -u 1000 -m -s /bin/bash bbb
   ```

   This will give the new user `bbb` the same UID as `aaa`, but it will also create a conflict in the `/etc/passwd` file because both `aaa` and `bbb` will have the same UID. The system doesn't allow multiple users with the same UID in normal situations.

2. **Resolve the conflict**:
   You can't have two users with the same UID (unless you manually resolve this in the `/etc/passwd` file, but it's not recommended and could cause issues). Therefore, you need to modify the UID of either `aaa` or `bbb` if you want both users to exist on the system.

   You could choose to update the UID of `aaa` (the existing sudoer), keeping `bbb` as a new user with UID 1000.

   **Change the UID of `aaa`**:

   ```
   sudo usermod -u 1001 aaa
   ```

   Then, you can proceed to create the `bbb` user with UID 1000 as originally intended.

3. **Create user `bbb` with UID 1000**:
   Now that the conflict is resolved (by changing `aaa`'s UID), create `bbb`:

   ```
   sudo useradd -u 1000 -m -s /bin/bash bbb
   ```

4. **Set a password for `bbb`**:

   ```
   sudo passwd bbb
   ```

5. **Ensure `bbb` is not a sudoer**:
   Make sure `bbb` is not part of any sudo-related group (i.e., `sudo`, `wheel`, etc.):

   ```
   sudo deluser bbb sudo
   sudo deluser bbb wheel
   ```

6. **Verify the UID and Groups**:
   After this, you can verify the UID and check the group memberships to make sure everything is correct:

   ```
   id aaa
   id bbb
   ```

   `bbb` should have UID 1000 and not belong to any sudoers group.

This should allow you to create a new user `bbb` with UID 1000, while keeping the existing `aaa` user and preventing `bbb` from being a sudoer.
