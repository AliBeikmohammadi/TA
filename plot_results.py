#!/usr/bin/env python
# coding: utf-8
import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
np.set_printoptions(precision=3, suppress=True)

Env= sys.argv[1]
Input_file_dir= sys.argv[2]
Save_fig_dir= sys.argv[3]
O_RT = float(sys.argv[4]) 
O_RA = float(sys.argv[5])

# Env='RW'
# Input_file_dir='/cephyr/users/alibe/Alvis/KDD2022/main/Results/RandomWalk/RW_s33_r100_e500.csv'
# Save_fig_dir='./Results/RandomWalk/'
# O_RT=1
# O_RA=0

print ('Env:', Env, '\nInput_file_dir:', Input_file_dir, '\nSave_fig_dir:', 
       Save_fig_dir, '\nShow O_RT:', O_RT, '\nShow O_RA:', O_RA)

def RW_plot(input_file_dir, save_fig_dir, o_RT, o_RA):
    with open(input_file_dir, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        data = list(reader)
    data=np.array(data).astype(float)
    episode = np.amax(data[:,3]).astype(int)

    only_RT, only_RA, TA = [], [], []
    for i in range(len(data)):
        if data[i,1]==0 and data[i,2]==0:
            only_RT.append(data[i])
        if data[i,1]==1 and data[i,2]==1:
            only_RA.append(data[i])
        if (not(data[i,1]==1 and data[i,2]==1)) and (not(data[i,1]==0 and data[i,2]==0)):
            TA.append(data[i])

    name=input_file_dir.split("/")[-1][:-4]
    nstate=name.split("_")[1][1:]
    isExist = os.path.exists(save_fig_dir)
    if not isExist:
        os.makedirs(save_fig_dir)
    rt=np.array(only_RT)
    ra=np.array(only_RA)
    ta=np.array(TA)
    plt.figure(figsize=[10, 7], dpi=72)
    if rt.size == 0:
        print('Warning: There are no Only R_T Results in inserted address')
    if ra.size == 0:
        print('Warning: There are no Only R_A Results in inserted address')
    if o_RT==1 and (not rt.size == 0):
        plt.plot(rt[:,3], rt[:,5],'.', label=r'Only $R^T$ (Baseline)',linewidth=3, c='k')
    if o_RA==1 and (not ra.size == 0):
        plt.plot(ra[:,3], ra[:,5],'-.', label=r'Only $R^A$',linewidth=3, c='gray') 
    for i in range(int(len(ta)/episode)):
        plt.plot(ta[i*episode:(i+1)*episode ,3], ta[i*episode:(i+1)*episode ,5], 
                 label=r'TA-Explore with $λ = {}$'.format(ta[i*episode,2]),linewidth=3)    

    plt.margins(.05)
    plt.xlabel('Walks / Episodes')
    plt.ylabel('RMS error')
    plt.legend()
    plt.title("RMS error of Random Walk ({} States)".format(nstate))
    plt.rcParams.update({'font.size': 15})  
    plt.savefig(save_fig_dir+name+'.png', dpi=144, format=None, metadata=None,
        bbox_inches=None, pad_inches=0.1,
        facecolor='auto', edgecolor='auto',
        backend=None)
    
    plt.figure()
    for i in range(int(len(ta)/episode)):
        plt.plot(ta[i*episode:(i+1)*episode ,3], ta[i*episode:(i+1)*episode ,4], 
                 label=r'$\beta(0)= {}, λ = {}$'.format(ta[i*episode,1], ta[i*episode,2]),linewidth=3)  
    plt.xlabel('Episodes')
    plt.ylabel(r'$\beta(t)$')
    plt.legend()
    plt.title(r'$\beta(t) = \beta(0)\lambda^{e}$ for Random Walk')
    plt.rcParams.update({'font.size': 15})
    plt.savefig(save_fig_dir+name+'beta.png', dpi=144, format=None, metadata=None, bbox_inches=None, 
                pad_inches=0.1, facecolor='auto', edgecolor='auto',backend=None)  

if Env=='RW':
    RW_plot(input_file_dir=Input_file_dir, save_fig_dir=Save_fig_dir,o_RT=O_RT,o_RA=O_RA)

