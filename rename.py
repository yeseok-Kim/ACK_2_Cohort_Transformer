from pathlib import Path

RENAME = {
    # 아직 치환 안 한 경우
    'sales_lag_1': 'sales_m_0', 'sales_lag_2': 'sales_m_1', 'sales_lag_3': 'sales_m_2',
    'orders_lag_1': 'orders_m_0', 'orders_lag_2': 'orders_m_1', 'orders_lag_3': 'orders_m_2',
    'quantity_lag_1': 'quantity_m_0',
    # 이미 m0으로 바꾼 경우
    'sales_m0': 'sales_m_0', 'sales_m1': 'sales_m_1', 'sales_m2': 'sales_m_2',
    'orders_m0': 'orders_m_0', 'orders_m1': 'orders_m_1', 'orders_m2': 'orders_m_2',
    'quantity_m0': 'quantity_m_0',
}

TARGETS = ['repurchase_weekly_prob.ipynb', 'RFM_4rd_processed.ipynb']

for name in TARGETS:
    f = Path(name)
    s = f.read_text(encoding='utf-8')
    n = sum(s.count(k) for k in RENAME)
    for old, nw in RENAME.items():
        s = s.replace(old, nw)
    f.write_text(s, encoding='utf-8')
    print(f'{name}: {n}건 치환')