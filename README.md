# README

How to setup the script?

```
chmod +x wa.py
```

To run:

```
./wa.py 919822012345
./wa.py +91-98220 12345
./wa.py 9822012345
```


# Setting up to run from anywhere (on a Mac)


1. First, let's find out your username. Run this command:

   ```
   whoami
   ```

   This will output your username.

2. Now, use your actual username in place of `$USER` in the chown command. 
Replace `yourusername` with the output from the `whoami` command:

   ```
   sudo chown yourusername:staff /usr/local/bin/wa
   ```

3. Then, set the correct permissions:

   ```
   sudo chmod 755 /usr/local/bin/wa
   ```

4. Verify the changes:

   ```
   ls -l /usr/local/bin/wa
   ```

   You should see output similar to this (with your actual username):

   ```
   -rwxr-xr-x  1 yourusername  staff  1166 Oct  8 11:13 /usr/local/bin/wa
   ```

5. Now try running the command:

   ```
   wa 9822012345
   ```

This should resolve the permission issues, allowing you to run the `wa` command without `sudo`.