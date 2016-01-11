#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import argparse
import arghelper

def excute_sh(host, user, password):
    cmd = "./ssh_excute.sh %s %s %s" % (host, user, password)
    print "Exe command:%s" % cmd
    stream = os.popen(cmd).read()
    return None

def excute_scp(host, user, password, sf, df):
    cmd = "./scp_excute.sh %s %s %s %s %s" % (host, user, password, sf, df)
    print "Exe command:%s" % cmd
    stream = os.popen(cmd).read()
    return None

def _file_read(file_path):
    with open(file_path) as f:
        fd = f.read()
    for com_nod in fd.split('\n'):
        if com_nod:
            yield com_nod.split(' ')

def main():
    c_type, lf, sf, df = args_parser()
    if c_type == "scp" and (sf and df):
        for host, username, password in _file_read(lf):
            excute_scp(host, username, password, sf, df)
    elif c_type == "ssh_excute":
        for host, username, password in _file_read(lf):
            excute_sh(host, username, password)
    else:
        print "匹配失败"
    return None


def args_parser():
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument("c_type", choices=['scp', 'ssh_excute'],
                        help="操作的类型 scp/ssh执行脚本")

    parser.add_argument("-lf", help="目标列表路径")
    parser.add_argument("-df", help="目的路径")
    parser.add_argument("-sf", help="源路径")
    args = parser.parse_args()
    return args.c_type, args.lf, args.sf, args.df

if __name__ == "__main__":
    main()
