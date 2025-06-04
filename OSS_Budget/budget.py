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

    def category_detail(self, selected, summary):
        if selected not in summary:
                print("해당 카테고리가 없습니다. 다시 입력하세요.\n")
                return
        print(f"\n[{selected}] 카테고리 상세 내역")
        for e in self.expenses:
            if e.category == selected:
                print(e)      

    def category_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        while True:
            summary = {}
            for e in self.expenses:
                summary[e.category] = summary.get(e.category, 0) + e.amount

            print("\n[카테고리별 지출 합계]")
            for category, total in summary.items():
                print(f"{category}: {total}원")
            print()
            detailYN = input("상세 조회하려면 \"/F\", 메뉴로 돌아가려면 아무 키나 누르세요: ").strip()
            if detailYN == "/F":
                selected = input("상세 조회할 카테고리명을 입력하세요: ").strip()
                self.category_detail(selected, summary)
            else:
                break

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


