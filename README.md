# GetKolla
在使用kolla部署openstack时，在pull镜像时非常慢，该脚本旨在先解决镜像拖拽问题，批量获取所有目标版本所需的镜像并push到私有仓库，再安装时便可以直接从私有仓库pull。

## 获取所有镜像
运行getDockerImg.py脚本，会自动将所有的kolla镜像名字保存到本地txt文件。

## 筛选目标版本镜像pull到本地
修改pull.sh中的筛选条件，修改stein为目标制定版本即可，运行pull.sh批量获取所有镜像。

### 所有镜像都pull到本地后，可以批量在push到自己私有仓库。
