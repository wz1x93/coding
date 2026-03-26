import re
from datetime import datetime
import numpy as np

TRANSACTION_DATA = """
定投2026-03-23100.00交易进行中3.2212
买入2026-03-23100.00交易进行中3.2212
定投2026-03-20100.00-3.6121
买入2026-03-20100.00-3.6121
买入2026-03-201,000.00-3.6121
定投2026-03-19100.00-3.6845
买入2026-03-19100.00-3.6845
买入2026-03-191,000.00-3.6845
买入2026-03-191,000.00交易关闭3.6845
定投2026-03-18100.00-3.8558
买入2026-03-18100.00-3.8558
定投2026-03-17100.00-3.8700
买入2026-03-17100.00-3.8700
定投2026-03-16100.00-3.8666
买入2026-03-16100.00-3.8666
买入2026-03-161,000.00-3.8666
定投2026-03-13100.00-3.9239
买入2026-03-13100.00-3.9239
定投2026-03-12100.00-3.9753
买入2026-03-12100.00-3.9753
定投2026-03-11100.00-3.9898
买入2026-03-11100.00-3.9898
定投2026-03-10100.00-3.9703
买入2026-03-10100.00-3.9703
定投2026-03-09100.00-3.9543
买入2026-03-09100.00-3.9543
买入2026-03-061,000.00-3.9519
定投2026-03-05100.00-3.9866
买入2026-03-05100.00-3.9866
定投2026-03-04100.00-3.9984
买入2026-03-04100.00-3.9984
定投2026-03-03100.00-4.0995
买入2026-03-03100.00-4.0995
定投2026-03-02100.00-4.1518
买入2026-03-02100.00-4.1518
定投2026-02-27100.00-3.9640
买入2026-02-27100.00-3.9640
定投2026-02-26100.00-3.9691
买入2026-02-26100.00-3.9691
定投2026-02-25100.00-3.9731
买入2026-02-25100.00-3.9731
定投2026-02-24100.00-3.9802
定投2026-02-13100.00-3.8481
买入2026-02-131,000.00-3.8481
定投2026-02-12100.00-3.8967
定投2026-02-11100.00-3.8979
定投2026-02-10100.00-3.8768
定投2026-02-09100.00-3.8737
买入2026-02-061,000.00-3.7946
买入2026-02-051,000.00-3.8375
定投2026-02-04100.00-3.9535
买入2026-02-0410,000.00-3.9535
定投2026-02-03100.00-3.8065
定投2026-02-02100.00-3.5806
定投2026-02-01100.00-暂无数据
定投2026-01-30100.00-暂无数据
定投2026-01-29100.00-4.2992
买入2026-01-2920,000.00-4.2992
定投2026-01-28100.00-4.0988
定投2026-01-27100.00-3.9651
定投2026-01-2650.00-3.9645
买入2026-01-2610,000.00-3.9645
定投2026-01-2350.00-3.8489
定投2026-01-2250.00-3.7595
定投2026-01-2150.00-3.7723
定投2026-01-2050.00-3.6655
定投2026-01-1950.00-3.6293
定投2026-01-1650.00-3.5855
定投2026-01-1550.00-3.5908
定投2026-01-1450.00-3.6033
定投2026-01-1350.00-3.5597
定投2026-01-1250.00-3.5536
定投2026-01-0950.00-3.4839
定投2026-01-0850.00-3.4599
定投2026-01-0750.00-3.4724
定投2026-01-0650.00-3.4828
定投2026-01-0550.00-3.4505
定投2026-01-0450.00-暂无数据
定投2026-01-0350.00-暂无数据
定投2025-11-1950.00-3.2518
定投2025-11-1850.00-3.1908
定投2025-11-1750.00-3.2391
定投2025-11-1450.00-3.2985
定投2025-11-1350.00-3.3338
"""

def parse_transactions(data_str):
    lines_data = []
    for line in data_str.strip().split('\n'):
        line = line.strip()
        if not line or '交易类型' in line:
            continue
        match = re.match(r'(定投|买入|卖出)(\d{4}-\d{2}-\d{2})([\d,]+\.\d{2})(.*?)([-]?\d+\.\d+|暂无数据)', line)
        if match:
            typ, date_str, amount_str, _, nav_str = match.groups()
            if nav_str != '暂无数据':
                try:
                    amount = float(amount_str.replace(',', ''))
                    nav = abs(float(nav_str))  # 处理可能的“-”分隔符
                    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                    lines_data.append((date_obj, typ, amount, nav))
                except ValueError:
                    pass
    # 按日期升序处理（确保买入在前、卖出在后）
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

class GoldDCAStrategy:
    def __init__(self, base_daily=250.0, max_daily=5000.0):
        self.total_cost, self.total_shares = parse_transactions(TRANSACTION_DATA)
        avg_cost = self.total_cost / self.total_shares if self.total_shares > 0 else 0
        print(f"【解析成功】从表格自动计算得到：总成本 {self.total_cost:.2f} 元 | 总份额 {self.total_shares:.2f} 份 | 平均成本 {avg_cost:.4f} 元")
        self.base_daily = base_daily
        self.max_daily = max_daily
        self.annual_mu = 0.08      # 可调整：乐观12%、保守4%
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
        current_value = self.total_shares * current_nav
        pnl_pct = (current_value - self.total_cost) / self.total_cost * 100 if self.total_cost > 0 else 0
        
        prob, median_days = self.monte_carlo_breakeven_prob(current_nav)
        
        discount = (avg_cost - current_nav) / avg_cost if avg_cost > 0 else 0
        factor = max(0.5, 1 + discount * 4)
        if prob < 60:
            factor *= 1.5
        elif prob > 80:
            factor *= 0.6
        
        buy_amount = min(self.base_daily * factor, self.max_daily)
        buy_amount = round(buy_amount / 50) * 50
        
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
        print(f"\n=== {datetime.now().date()} 决策报告 ===")
        print(f"当前NAV: {current_nav:.4f} | 平均成本: {avg_cost:.4f} | 浮盈/亏: {pnl_pct:+.2f}%")
        print(f"MC 90天回本概率: {prob:.1f}% | 预计中位回本天数: {median_days:.0f}天")
        print(signal)
        print(f"执行后新平均成本: {new_avg:.4f} | 新总份额: {self.total_shares:.2f} | 新总成本: {self.total_cost:.2f}")
        print("请立即在平台操作，并将今日交易（买入/卖出）按相同格式追加到 TRANSACTION_DATA 表格末尾，下次运行自动刷新持仓。")
        return buy_amount if '买入' in signal else 0

# ====================== 使用说明 ======================
# 1. 保存为 gold_dca_dynamic_v2.py
# 2. 每天14:30-15:00运行：python gold_dca_dynamic_v2.py
# 3. 输入今日最新单位净值
if __name__ == "__main__":
    strategy = GoldDCAStrategy()
    nav_input = float(input("请输入今日最新单位净值 (NAV, 如 3.2212): "))
    strategy.daily_decision(nav_input)
