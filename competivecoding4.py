n, m, a, b = map(int, input().split())
m_tickets = n // m
remaining_rides = n % m
min_cost = m_tickets * b + min(remaining_rides * a, b)

print(min_cost)