# Git学习

## 版本控制
版本控制是一个系统（VCS），它记录一个文件或一组文件随时间推移的更改，以便您以后可以调用特定版本。 要解决的问题就有保留文件的历史状态，方便修改以及多人协作开发的修改

## Git介绍
### 独特的数据处理方式
大多数是将所做的更改存储为一组文件，而Git将其数据更像是微型文件系统的一系列快照。Git 基本上都会拍摄所有文件在那一刻的样子，并存储对该快照的引用。 为了提高效率，如果文件没有更改，Git 不会再次存储该文件，而只是指向它已经存储的上一个相同文件的链接。

Git所有的数据操作基本是在本地进行的，而无需从服务器访问

Git 中的所有内容在存储之前都会进行校验和计算，然后由该校验和引用。 这意味着在 Git 不知道的情况下，不可能更改任何文件或目录的内容。

几乎所有操作都只向 Git 数据库添加数据。 很难让系统执行任何不可撤消的操作或使其以任何方式擦除数据。

### Git的三种主要状态

1. modified 已更改文件但尚未提交

1. stage 在当前版本中已提交了修改后的文件

1. committed 数据已安全的提交

### Git项目的三个主要部分
1. 工作区 a checkout of one version of the project.These files are pulled out for you to use or modified.

2. staging area（暂存区）保存了下次要提交的文件列表信息，在Git仓库目录中

3. Git仓库 保存项目的元数据和对象数据库的地方

### 工作流程
1. 在工作区中修改文件。

2. 将你想要下次提交的更改选择性地暂存，这样只会将更改的部分添加到暂存区。

3. 提交更新，找到暂存区的文件，将快照永久性存储到 Git 目录。
如果 Git 目录中保存着特定版本的文件，就属于 已提交 状态。 如果文件已修改并放入暂存区，就属于 已暂存 状态。 如果自上次检出后，作了修改但还没有放到暂存区域，就是 已修改 状态。

## 命令行
使用原生命令行模式或GUI模式（GUI只是一种降低难度的软件）

## 配置
检查配置信息请使用`git config --list`命令、
通过以下命令查看所有的配置以及他们的所在文件`git config --list --show-origin`

## 获取帮助
```
git help <verb>
git <verb> --help
man git-<verb>
```
获取`git config`命令手册可以通过执行`git help config`,`git add -h`可以获得简要参考

## Git基础操作

### 设置别名

对于一些常用的命令，如果它本身很长，我们输入起来不方便。为了简便使用，我们可以在.bashrc文件中写入```alias 命令别名 原命令```，即可简化我们的命令

设置完成后，使用```source ~/.bashrc```来初始化环境
### 创建账户和邮箱

```
git config --global user.name name
git config --global user.email email
```

### 获取Git仓库
1. 将没有进行版本控制的本地目录转换为git仓库
1. 克隆一个已有的仓库

#### 本地创建仓库
首先是进入已有的项目目录，在git-bash（终端或者cmd）中输入指令`cd E:\my_project`

使用命令`git init`进行初始化仓库

之后用命令`git add readme.txt`将已有项目提交到暂存区

再使用命令`git commit -m "xxx"`将项目提交，其中-m之后的内容是对于本次提交的说明

以上就是最简单的创建环节

#### 查看工作区状态并修改文件

通过命令`git status`可以查看仓库的状态，此时如果修改了文件内容运行该命令会得到
```
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working director
        modified:   readme.txt

no changes added to commit (use "git add" and/or "git commit -a")
```
告诉我们文件发生了修改

此时运行`git diff`就可以查看修改了什么

此时再运行`git add`命令就将文件加入了暂存区，再通过`git commit`命令就可以将我们修改后的文件提交到仓库。

#### 回溯

##### git log

查看历史记录，使用命令`git log`,会显示所有的提交日志。对命令加上参数`--pretty=online`可以简化输出

* -all：显示所有分支
* --pretty=online：显示为一行
* --abbrev-commit：是的输出的commitID更加简短
* --graph：以图的形式显示
  

对于结果中的一串十六进制数，是`commit id`（版本号），`HEAD`表示当前版本，而上一个版本表示为`HEAD^`，上上一个为`HEAD^^`，往上$n$个版本表示为`HEAD~n`  

##### 版本回退

回退到上一个版本，可以使用命令`git reset --hard HEAD^/commitid`，这里相关的有三个参数

* ```--hard```表示回退到上个版本的已提交状态
* `--soft`表示回退到未提交状态
* `--mixed`表示回退到已添加但未提交的状态

如果你回溯后悔了，也有办法，向上翻找未修改版本的版本号，再使用`git reset`命令即可，如果找不到该版本号，可使用命令`git reflog`可查找到每一次命令结果

#### 添加文件之忽略列表

对于一些文件我们并不关心，可以创建一个文件.gitignore，写入我们不关心的文件格式

### 分支

分支方便用于多人协作，之后再merge到main里。

#### 查看与创建

```git branch (name)```不添加分支名可以查看有哪些分支，加上分支名就可以创建新的分支。新创建的分支会完全复制已有的分支


#### 切换分支

切换分支```git checkout [-b] branchname```-b选项表示先创建新分支再切换

#### 合并分支

```git merge name1```将name1的分支合并到当前分支上

#### 解决冲突

对于两个不同的分支修改了同一个文件，合并时应该如何处理。

在直接使用```git merge branch```时就可能会引发conflict，此时如果没有额外的指令，冲突文件中在无法决定的位置会出现
```text
这是当前分支中的内容。
这是合并过来的分支中的内容。
```

此时，我们应当手动更改冲突文件，并重新进行add，commit

#### 分支规范

* master：主分支
* develop：所有的线上开发分支应该被提交到的develop

####  删除分支

```git branch -d/D <branch>```


### 远程仓库（常用github）

#### 配置公钥

```ssh-keygen -t rsa```不断回车就会生成密钥。在~/.ssh/id_rsa.pub中查看密钥。```ssh -T git@github.com```通过该命令可以检查SSH配置是否正常

#### 操作远程仓库

##### 添加

```git remote add <远端名称>(常用origin) <path>```github的常用路径：```github.com:<username>/<repositeroyname>.git```


若已经链接了别的仓库，可以先删除```git remote remove origin```

##### 查看

```git remote -v```会显示链接库的详细信息

##### 推送

```git push -u origin master:main```将origin的main与本地的master建立跟踪关系。在建立跟踪关系后就可以直接进行```git push```

##### 获取远程仓库文件

* clone：直接克隆一个远程仓库，相当于直接复制了该远程仓库的所有信息
* fetch：获取远端仓库的最新提交的信息，并会建立一个origin/<branchname>，不同于我们当前仓库的分支。相当于没有合并两个分支。如果想要合并，可以使用```git merge origin/main```
* pull：相当于pull+merge


