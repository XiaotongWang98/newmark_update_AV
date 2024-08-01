import numpy as np
import pandas as pd
import argparse

def calculate(alpha, delta, a0, v0, dt, input_file, output_file):
    # 读取CSV文件中的位移数据
    df = pd.read_csv(input_file)
    u = df['displacement'].values 
    
    # 定义速度和加速度的初值
    v = np.zeros_like(u)
    a = np.zeros_like(u)
    v[0] = v0
    a[0] = a0

    # 计算系数
    a0_coef = 1 / (alpha * dt**2)
    a2_coef = 1 / (alpha * dt)
    a3_coef = 1 / (2 * alpha) - 1
    a4_coef = delta / alpha - 1
    a5_coef = dt / 2 * (delta / alpha - 2)
    a6_coef = dt * (1 - delta)
    a7_coef = delta * dt

    # 计算加速度和速度
    for i in range(1, len(u)):
        a[i] = a0_coef * (u[i] - u[i - 1]) - a2_coef * v[i - 1] - a3_coef * a[i - 1]
        v[i] = v[i - 1] + a6_coef * a[i - 1] + a7_coef * a[i]

    # 将结果保存到CSV文件
    result_df = pd.DataFrame({'displacement': u, 'velocity': v, 'acceleration': a})
    result_df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Newmark Method Calculation")
    parser.add_argument('--alpha', type=float, required=True, help="Alpha parameter")
    parser.add_argument('--delta', type=float, required=True, help="Delta parameter")
    parser.add_argument('--a0', type=float, required=True, help="Initial acceleration")
    parser.add_argument('--v0', type=float, required=True, help="Initial velocity")
    parser.add_argument('--dt', type=float, required=True, help="Time step")
    parser.add_argument('--input_file', type=str, required=True, help="Input CSV file with displacement data")
    parser.add_argument('--output_file', type=str, required=True, help="Output CSV file for results")
    
    args = parser.parse_args()
    calculate(args.alpha, args.delta, args.a0, args.v0, args.dt, args.input_file, args.output_file)
