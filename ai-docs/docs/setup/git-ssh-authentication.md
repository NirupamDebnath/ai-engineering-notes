# GitHub SSH authentication for Git CLI

This page shows how to set up SSH authentication for GitHub when using the Git CLI on Linux.

It covers:

- checking or generating SSH keys
- adding the key to the SSH agent
- registering the key with GitHub
- testing your SSH connection
- using SSH remote URLs for repositories
- troubleshooting common issues

## 1. Check for an existing SSH key

Run:

```bash
ls -al ~/.ssh
```

Look for:

- `id_ed25519` / `id_ed25519.pub`
- `id_rsa` / `id_rsa.pub`

If you already have a key, you can reuse it for GitHub. If you want a dedicated key, generate a new one.

## 2. Generate a new SSH key (recommended)

Use the modern `ed25519` algorithm:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

When prompted:

- Accept the default file location by pressing Enter
- Add a passphrase for extra security (recommended)

This creates:

- private key: `~/.ssh/id_ed25519`
- public key: `~/.ssh/id_ed25519.pub`

> If you need compatibility with older systems, use `ssh-keygen -t rsa -b 4096` instead.

## 3. Add the SSH key to the agent

Start the SSH agent and add the key:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

If you reused an existing key, substitute its filename accordingly.

## 4. Add the public key to GitHub

Copy the public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Then in GitHub:

1. Go to **Settings**
2. Open **SSH and GPG keys**
3. Click **New SSH key**
4. Paste the public key
5. Give it a descriptive title, such as `mx-linux-laptop`

## 5. Test the SSH connection

Run:

```bash
ssh -T git@github.com
```

A successful response looks like:

```text
Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.
```

If you see `Permission denied (publickey)`, double-check your key and agent status.

## 6. Use SSH remote URLs for Git

Clone over SSH instead of HTTPS:

```bash
git clone git@github.com:your-username/your-repo.git
```

If an existing repo uses HTTPS, switch it:

```bash
git remote set-url origin git@github.com:your-username/your-repo.git
```

## 7. Configure Git identity (optional)

If you have not already configured your Git identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

## 8. Troubleshooting

### Permission denied (publickey)

```bash
ssh-add ~/.ssh/id_ed25519
```

Also verify the agent is running and the correct key is loaded.

### Remote still uses HTTPS

```bash
git remote -v
```

Then update the remote URL if needed:

```bash
git remote set-url origin git@github.com:username/repo.git
```

### SSH key does not load automatically

Add this to your shell config (`~/.bashrc`, `~/.zshrc`):

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

## 9. Optional: use `~/.ssh/config`

If you manage multiple SSH keys or accounts, add a host entry:

```bash
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
```

## Notes

- The page is intentionally specific to GitHub and Git CLI.
- Keep the file in `ai-docs/docs/setup/` as the correct folder for setup instructions.
