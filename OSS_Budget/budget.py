import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def expense_summary(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        amounts = [e.amount for e in self.expenses]
        count = len(amounts)
        total = sum(amounts)
        avg = total / count

        min_expense = min(self.expenses, key=lambda e: e.amount)
        max_expense = max(self.expenses, key=lambda e: e.amount)

        category_totals = {}
        for e in self.expenses:
            category_totals[e.category] = category_totals.get(e.category, 0) + e.amount
        top_category = max(category_totals.items(), key=lambda x: x[1])

        print("\n[지출 통계 요약]")
        print(f"총 지출 건수: {count}건")
        print(f"총 지출: {total}원")
        print(f"평균 지출: {avg:.2f}원")
        print(f"최소 지출: {min_expense.amount}원 - {min_expense.category} ({min_expense.description})")
        print(f"최대 지출: {max_expense.amount}원 - {max_expense.category} ({max_expense.description})")
        print(f"가장 많이 쓴 카테고리: {top_category[0]} ({top_category[1]}원)\n")


