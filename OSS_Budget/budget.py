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

    def edit_expenses(self, index):
        if index <0 or index>=len(self.expenses):
            print("유효하지 않은 입력입니다.\n")
            return

        origin = self.expenses[index]
        print("***수정하지 않을 항목에 대해서는 \"-1\"을 입력하세요.***\n")
        
        new_category = input("카테고리 (예: 식비, 교통 등): ").strip()
        if new_category != "-1":
            origin.category = new_category

        new_description = input("설명: ").strip()
        if new_description != "-1":
            origin.description = new_description

        new_amount = input("금액(원): ").strip()
        if new_amount != "-1":
            origin.amount = int(new_amount)
        print("수정되었습니다.")
        return

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        
        while True:
            print("\n[지출 목록]")
            for idx, e in enumerate(self.expenses, 1):
                print(f"{idx}. {e}")
            print()

            editYN = input("수정하려면 \"/E\", 메뉴로 돌아가려면 아무 키나 눌러주세요: ").strip()
            if editYN == "/E":
                try:
                    num = int(input("수정할 지출목록의 번호를 입력하세요: ").strip())
                    self.edit_expenses(num - 1)
                except ValueError:
                    print("숫자를 입력하세요.")
            else:
                break

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")
