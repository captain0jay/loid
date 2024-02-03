<img src="media/loidbanner.svg">

### Loid - Read, write and publish from your terminal.

Loid is a CLI tool that makes it easy to Read,write and publish blogs on hashnode without leaving the terminal. This project was made using Hashnode API for [Hashnode](https://hashnode.com/hackathons/apihackathon?source=hashnode-hackathons-listing) hackathon.

> :warning: - You need personal access token from hashnode to make Loid work.

> :package: - Check out <a href="https://pypi.org/project/loid/">Loid on PyPI</a>.

> :book: - Read loids blog <a href="https://captainjay.hashnode.dev/loid-read-write-and-publish-blogs-on-hashnode-straight-from-your-terminal">Here</a>.

### Installation
Make sure you have `pip` and `python>=3.6` installed on your machine and follow the steps.

<details>
  <summary><h4>1. Setup the package</h4></summary>

##### Download from PyPI archive
```sh
pip install -U loid
```
or

##### Download from GitHub archive
```sh
pip install git+http://github.com/captain0jay/loid.git
```

> :warning:: Loid is POSIX-friendly. It might not work properly on the Windows machines at the moment.

</details>

<details>
  <summary><h4>2. Set the <code>BLOG_DOMAIN</code> environment variable</h4></summary>

After the package installed on your system, it's time to add the `BLOG_DOMAIN` environment variable. Create an account on [hashnode.com](https://hashnode.com/), replace your email with `<HASHNODE_BLOG_DOMAIN>` in the following options.

##### > If you use the default bash shell
```sh
echo "export BLOG_DOMAIN=<HASHNODE_BLOG_DOMAIN>" >> ~/.bashrc
```
##### > If you use ZSH
```sh
echo "export BLOG_DOMAIN=<HASHNODE_BLOG_DOMAIN>" >> ~/.zshrc
```

</details>

<details>
  <summary><h4>3. Insert your personal access token</h4></summary>

Now, your account's Personal access token. Simply run `loid get` with `--auth` option and enter your Personal access token.

```sh
loid get --auth
```

</details>

### Exiting from editor or viewer

If for some reason Ctrl + q doesn't work for quitting the editor Ctrl + c should be used it will give the error but ignore it for time being it will get fixed soon

Update:

1. Whenever you are viewing posts from loid get --feed or loid publication example.com you have to press Q and then Enter to exit

2. while when you are fetching posts or draft separately just press Q to exit

3. When you have opened an editor to edit your draft press Ctrl + q to exit

### Usage
Use `loid` with commands from the list given here to perform various tasks avilable on hashnode

```
$ loid create newdraft
Empty Markdown file 'newdraft.md' created in the 'drafts' folder.
```
using below command will open an editor which you can edit and save using 'Ctrl + s' and quit using 'Ctrl + q'
```
$ loid open newdraft
```
To publish already created offline draft
```
$ loid publish newdraft
```
Returns publication post with title and id that you can select and read in your terminal
```
$ loid publication captainjay.hashnode.dev
```
To publish drafts already available in your hashnode account (you can get id using 'loid get --listonlinedrafts')
```
$ loid publishonlinedraft 000000000000000000
```
You can read online draft avilable in your account but cannot edit due to the functionality not being made available yet by hashnode as soon as they release it, it will be available.
```
$ loid readDraft 000000000000000000
```
You can read any posts available on hashnode (you can get id using 'loid get --feed' or 'loid publication example.hashnode.com')
```
$ loid readPost 000000000000000000
```
List offline drafts with modification time 
```
$ loid get --drafts
```
Get articles from your feed and select to read them its that easy :)
```
$ loid get --feed
```
Get your drafts that are stored online on hashnode account
```
$ loid get --listonlinedrafts
```
Returns current version of Loid
```
$ loid get --version
```
### License
Loid is being licensed under the [MIT License](https://github.com/captain0jay/loid/blob/main/LICENSE).

### Special Thanks to
[Hashnode](https://hashnode.com) for hosting this great hackathon.
