import re
from datetime import datetime
import numpy as np

TRANSACTION_DATA = """
定投 2026-03-26 1000.00 3.4442
定投 2026-03-26 100.00 3.4442
定投 2026-03-25 100.00 3.5224
定投 2026-03-24 100.00 3.3988
定投 2026-03-23 100.00 3.2212
定投 2026-03-20 100.00 3.6121
定投 2026-03-20 100.00 3.6121
定投 2026-03-19 1000.00 3.6845
定投 2026-03-19 100.00 3.6845
定投 2026-03-18 100.00 3.8558
定投 2026-03-17 100.00 3.8700
定投 2026-03-16 1000.00 3.8666
定投 2026-03-16 100.00 3.8666
定投 2026-03-13 1000.00 3.9239
定投 2026-03-13 100.00 3.9239
定投 2026-03-12 100.00 3.9753
定投 2026-03-11 100.00 3.9898
定投 2026-03-10 100.00 3.9703
定投 2026-03-09 100.00 3.9543
定投 2026-03-06 1000.00 3.9519
定投 2026-03-06 100.00 3.9519
定投 2026-03-05 100.00 3.9866
定投 2026-03-04 100.00 3.9984
定投 2026-03-03 100.00 4.0995
定投 2026-03-02 100.00 4.1518
定投 2026-02-27 100.00 3.9640
定投 2026-02-26 100.00 3.9691
定投 2026-02-25 100.00 3.9731
定投 2026-02-24 100.00 3.9802
定投 2026-02-13 1000.00 3.8481
定投 2026-02-13 100.00 3.8481
定投 2026-02-12 100.00 3.8967
定投 2026-02-11 100.00 3.8979
定投 2026-02-10 100.00 3.8768
定投 2026-02-09 100.00 3.8737
定投 2026-02-06 1000.00 3.7946
定投 2026-02-05 1000.00 3.8375
定投 2026-02-04 10000.00 3.9535
定投 2026-02-04 100.00 3.9535
定投 2026-02-03 100.00 3.8065
定投 2026-02-02 100.00 3.5806
定投 2026-01-30 100.00 4.0398
定投 2026-01-29 20000.00 4.2992
定投 2026-01-29 100.00 4.2992
定投 2026-01-28 100.00 4.0988
定投 2026-01-27 100.00 3.9651
定投 2026-01-26 10000.00 3.9645
定投 2026-01-26 50.00 3.9645
定投 2026-01-23 50.00 3.8489
定投 2026-01-22 50.00 3.7595
定投 2026-01-21 50.00 3.7723
定投 2026-01-20 50.00 3.6655
定投 2026-01-19 50.00 3.6293
定投 2026-01-16 50.00 3.5855
定投 2026-01-15 50.00 3.5908
定投 2026-01-14 50.00 3.6033
定投 2026-01-13 50.00 3.5597
定投 2026-01-12 50.00 3.5536
定投 2026-01-09 50.00 3.4839
定投 2026-01-08 50.00 3.4599
定投 2026-01-07 50.00 3.4724
定投 2026-01-06 50.00 3.4828
定投 2026-01-05 50.00 3.4505
定投 2025-12-31 50.00 3.3881
定投 2025-12-30 50.00 3.4121
定投 2025-12-29 50.00 3.4894
定投 2025-12-26 50.00 3.4995
定投 2025-12-25 50.00 3.4846
定投 2025-12-24 50.00 3.5017
定投 2025-12-23 50.00 3.4982
定投 2025-12-22 50.00 3.4477
定投 2025-12-19 50.00 3.3898
定投 2025-12-18 50.00 3.3902
定投 2025-12-17 50.00 3.3808
定投 2025-12-16 50.00 3.3547
定投 2025-12-15 50.00 3.3948
定投 2025-12-12 50.00 3.3510
定投 2025-12-11 50.00 3.3114
定投 2025-12-10 50.00 3.3059
定投 2025-12-09 50.00 3.2930
定投 2025-12-08 50.00 3.3167
定投 2025-12-05 50.00 3.3244
定投 2025-12-04 50.00 3.3009
定投 2025-12-03 50.00 3.3041
定投 2025-12-02 50.00 3.3203
定投 2025-12-01 50.00 3.3320
定投 2025-11-28 50.00 3.2966
定投 2025-11-27 50.00 3.2817
定投 2025-11-26 50.00 3.2733
定投 2025-11-25 50.00 3.2737
定投 2025-11-24 50.00 3.2203
定投 2025-11-21 50.00 3.2161
定投 2025-11-20 50.00 3.2352
定投 2025-11-19 50.00 3.2518
定投 2025-11-18 50.00 3.1908
定投 2025-11-17 50.00 3.2391
定投 2025-11-14 50.00 3.2985
定投 2025-11-13 50.00 3.3338
"""

import re
from datetime import datetime
import numpy as np

# ================= 数据解析部分 =================

def parse_transactions(data_str):
    lines_data = []
    # 正则表达式：匹配 交易类型 日期 金额 净值
    pattern = re.compile(r'^(定投|买入|卖出)\s+(\d{4}-\d{2}-\d{2})\s+([\d,]+\.\d{2})\s+([-]?\d+\.\d+)')

    for line in data_str.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
            
        match = pattern.match(line)
        if match:
            typ, date_str, amount_str, nav_str = match.groups()
            
            try:
                amount = float(amount_str.replace(',', ''))
                nav = abs(float(nav_str)) 
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                
                lines_data.append((date_obj, typ, amount, nav))
            except ValueError as e:
                print(f"数据解析错误: {line}, 原因: {e}")
                continue

    # 按日期升序处理
    lines_data.sort(key=lambda x: x[0])
    
    total_cost = 0.0
    total_shares = 0.0
    
    for _, typ, amount, nav in lines_data:
        if typ in ['定投', '买入']:
            shares_add = amount / nav
            total_cost += amount
            total_shares += shares_add
            
        elif typ == '卖出' and total_shares > 0:
            shares_sell = amount / nav
            if shares_sell > total_shares:
                shares_sell = total_shares
            
            avg_cost = total_cost / total_shares if total_shares > 0 else 0
            cost_remove = shares_sell * avg_cost
            
            total_cost -= cost_remove
            total_shares -= shares_sell

    return total_cost, total_shares

# ================= 策略类部分 =================

class GoldDCAStrategy:
    def __init__(self, base_daily=250.0, max_daily=5000.0):
        # 这里假设 TRANSACTION_DATA 已经在外部定义并赋值
        try:
            self.total_cost, self.total_shares = parse_transactions(TRANSACTION_DATA)
        except NameError:
            print("错误: 未找到 TRANSACTION_DATA 变量，请确保在运行前定义了交易数据字符串。")
            self.total_cost, self.total_shares = 0, 0
            
        avg_cost = self.total_cost / self.total_shares if self.total_shares > 0 else 0
        print(f"【解析成功】从表格自动计算得到：总成本 {self.total_cost:.2f} 元 | 总份额 {self.total_shares:.2f} 份 | 平均成本 {avg_cost:.4f} 元")
        self.base_daily = base_daily
        self.max_daily = max_daily
        self.annual_mu = 0.08
        self.annual_vol = 0.20

    def get_current_avg_cost(self):
        return self.total_cost / self.total_shares if self.total_shares > 0 else 0

    def monte_carlo_breakeven_prob(self, current_nav, days=90, n_sims=1000):
        avg_cost = self.get_current_avg_cost()
        daily_mu = self.annual_mu / 252
        daily_vol = self.annual_vol / np.sqrt(252)
        shocks = np.random.randn(n_sims, days) * daily_vol
        log_returns = daily_mu - 0.5 * daily_vol**2 + shocks
        sim_nav = current_nav * np.exp(np.cumsum(log_returns, axis=1))
        reached = np.any(sim_nav >= avg_cost, axis=1)
        prob = np.mean(reached) * 100
        days_to_hit = np.argmax(sim_nav >= avg_cost, axis=1)
        median_days = np.median(days_to_hit[days_to_hit > 0]) if np.any(days_to_hit > 0) else days
        return prob, median_days

    def daily_decision(self, current_nav):
        avg_cost = self.get_current_avg_cost()
        
        # --- 新增：计算持仓市值和累计盈亏金额 ---
        current_value = self.total_shares * current_nav
        pnl_abs = current_value - self.total_cost  # 正数为赚，负数为亏
        pnl_pct = (pnl_abs / self.total_cost * 100) if self.total_cost > 0 else 0
        # --------------------------------------
        
        prob, median_days = self.monte_carlo_breakeven_prob(current_nav)
        
        discount = (avg_cost - current_nav) / avg_cost if avg_cost > 0 else 0
        factor = max(0.5, 1 + discount * 4)
        if prob < 60:
            factor *= 1.5
        elif prob > 80:
            factor *= 0.6
        
        buy_amount = min(self.base_daily * factor, self.max_daily)
        buy_amount = round(buy_amount / 50) * 50
        
        signal = ""
        if current_nav >= avg_cost * 1.05:
            sell_shares = round(self.total_shares * 0.15, 2)
            sell_amount = round(sell_shares * current_nav, 2)
            signal = f"【卖出信号】卖出 {sell_shares} 份（约 {sell_amount} 元），锁定利润"
            avg = self.get_current_avg_cost()
            cost_remove = sell_shares * avg
            self.total_cost -= cost_remove
            self.total_shares -= sell_shares
        elif current_nav > avg_cost * 1.02:
            signal = f"【持仓观望】NAV已接近/超过成本，无需买入"
            buy_amount = 0
        else:
            signal = f"【买入信号】买入 {buy_amount} 元（动态DCA）"
            new_shares = buy_amount / current_nav
            self.total_cost += buy_amount
            self.total_shares += new_shares
        
        new_avg = self.get_current_avg_cost()
        
        # --- 修改：打印输出增加亏损总额显示 ---
        print(f"\n=== {datetime.now().date()} 决策报告 ===")
        print(f"当前NAV: {current_nav:.4f} | 平均成本: {avg_cost:.4f}")
        # 显示持仓市值和累计盈亏（金额）
        print(f"当前持仓市值: {current_value:.2f} 元 | 累计盈亏: {pnl_abs:+.2f} 元 ({pnl_pct:+.2f}%)")
        print(f"MC 90天回本概率: {prob:.1f}% | 预计中位回本天数: {median_days:.0f}天")
        print(signal)
        print(f"执行后新平均成本: {new_avg:.4f} | 新总份额: {self.total_shares:.2f} | 新总成本: {self.total_cost:.2f}")
        print("请立即在平台操作，并将今日交易（买入/卖出）按相同格式追加到 TRANSACTION_DATA 表格末尾，下次运行自动刷新持仓。")
        
        return buy_amount if '买入' in signal else 0

# ====================== 使用说明与测试 ======================
if __name__ == "__main__":
    strategy = GoldDCAStrategy()
    # 模拟输入一个净值，例如 3.1000 (低于成本，显示亏损)
    nav_input = float(input("请输入今日最新单位净值 (NAV, 如 3.2212): "))
    strategy.daily_decision(nav_input)
