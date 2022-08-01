# git环境搭建

<!-- toc -->

## 安装git

### Ubuntu

安装最新版的git

``` bash
$ apt update
$ apt install git
```

### Windows

下载最新版[git](https://github.com/git-for-windows/git/releases/download/v2.16.2.windows.1/Git-2.16.2-64-bit.exe), 直接运行安装即可

## 创建ssh-key

可参考github上的创建方法：

``` bash
$ ssh-keygen -t rsa -b 4096
```

保持默认即可，随后，ssh-key将存放于每个人的home目录下

``` bash
cat ~/.ssh/id_rsa.pub 
```

对于Windows系统，如果在安装git的时候选择安装了linux bash的话，使用方法同Linux。否则，可直接使用文本编辑器打开


## 向github添加ssh-key


### 环境配置
在Linux/Windows PC上执行
``` bash
git config --global user.name "your name"
git config --global user.email "your.mail@xxx.com"
```

## Git使用方法

### Step by step

#### 获取代码

``` bash
$ git clone https://github.com/simble1986/LearningPython.git
```
#### 更新代码
当你开始创建自己的代码时，应当使用git pull命令来更新本地代码库，使其与服务器上的一致
``` bash
$ cd study
$ git pull
```

#### 创建自己的脚本归档目录
``` bash
$ cd study
$ mkdir xxx
```

#### 新建脚本
``` bash
$ touch test1.py
```

#### 查看状态
养成一个良好的习惯，常用git status查看当前处于什么状态

``` bash
study# git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

    README.md

nothing added to commit but untracked files present (use "git add" to track)
```
注意提示信息只能够提到`use "git add <file>..." to include in what will be committed`，让你使用git add命令来将README.md加入到仓库中

#### 增加文件或目录

当新创建文件或目录后，需要手工将其加入到git跟踪数据库中
``` bash
$ git add <Your File>
```

#### 提交更改

使用git commit来提交更改，只是将当前的代码改动在本地保存起来，并不会提交到服务器上

**你可以多次提交更改**
但不必提交到git服务器上

* 命令行模式

``` bash
$ git commit -m "add README"
[master (root-commit) dd47147] Add Readme
 1 file changed, 122 insertions(+)
 create mode 100644 README.md
```

* 编辑器模式
编辑器模式会根据你的编辑器不同，操作方法略有不同

``` bash
$ git commit -a
```

当执行该命令后，将进入编辑器模式（Vim或Emacs），使用方法与编辑器保持一致，添加完内容后，保存退出即可

**明确的说明自己提交代码的原因是一个非常好的习惯**
#### 提交代码到服务器

``` bash
$ git push
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 1.87 KiB | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
```
