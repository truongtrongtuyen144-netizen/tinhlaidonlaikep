import streamlit as st

st.title("Tính lãi đơn và lãi kép")

# Nhập dữ liệu
C = st.number_input("Nhập số tiền gửi (đồng)", min_value=0.0, value=1000000.0)
i = st.number_input("Nhập lãi suất năm (%)", min_value=0.0, value=6.0) / 100
n = st.number_input("Nhập số tháng gửi", min_value=1, value=12)

# Nút tính toán
if st.button("Tính"):
    # Lãi đơn
    An = C * (i / 12 * n + 1)

    # Lãi kép
    Bn = C * (1 + i / 12) ** n

    st.subheader("Kết quả")
    st.success(f"Tổng số tiền theo phương pháp lãi đơn: {An:,.2f} đồng")
    st.success(f"Tổng số tiền theo phương pháp lãi kép: {Bn:,.2f} đồng")
