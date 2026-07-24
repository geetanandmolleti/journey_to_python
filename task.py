class Employee:
    company_name = "Global Tech Corp"
    total_employees = 0

    def __init__(self, emp_id, name, designation, current_ctc, months_exp, current_sal):
        Employee.total_employees += 1

        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.current_ctc = current_ctc
        self.months_exp = months_exp

        self.__current_sal = current_sal
        self.__revised_sal = current_sal

        self.hike_percentage = 0
        self.revised_ctc = current_ctc

        self.calculate_appraisal()

    @property
    def current_sal(self):
        return self.__current_sal

    @property
    def revised_sal(self):
        return self.__revised_sal

    @revised_sal.setter
    def revised_sal(self, value):
        self.__revised_sal = value

    def calculate_appraisal(self):
        if self.months_exp > 60:
            self.hike_percentage = 32
            self.revised_ctc = self.current_ctc * 1.32
            self.revised_sal = self.current_sal * 1.32

        elif self.months_exp > 38:
            self.hike_percentage = 24
            self.revised_ctc = self.current_ctc * 1.24
            self.revised_sal = self.current_sal * 1.24

        elif self.months_exp > 24:
            self.hike_percentage = 12
            self.revised_ctc = self.current_ctc * 1.12
            self.revised_sal = self.current_sal * 1.12

        elif self.months_exp == 12:
            self.hike_percentage = 0
            self.revised_ctc = 1.0
            self.revised_sal = 8.33

        elif self.months_exp < 12:
            self.hike_percentage = 0
            self.revised_sal = 30.0
            self.revised_ctc = 3.6

    def display_details(self):
        years_exp = round(self.months_exp / 12, 1)

        c_ctc = (
            f"{self.current_ctc}L"
            if self.current_ctc >= 1
            else f"{self.current_ctc * 100}k"
        )
        r_ctc = (
            f"{round(self.revised_ctc, 2)}L"
            if self.revised_ctc >= 1
            else f"{round(self.revised_ctc * 100, 2)}k"
        )

        print(
            f"Company: {self.company_name} | ID: {self.emp_id} | Name: {self.name} | Designation: {self.designation}"
        )
        print(
            f"Experience: {self.months_exp} Months ({years_exp} Years) | Hike Applied: {self.hike_percentage}%"
        )
        print(f"CTC Breakdown: Current: {c_ctc} ➔ Revised: {r_ctc}")
        print(
            f"In-Hand Sal  : Current: {self.current_sal}k ➔ Revised: {round(self.revised_sal, 2)}k"
        )
        print("-" * 85)


employees_list = [
    Employee(201, "Aarav Patel", "Director", 25.0, 72, 180.0),
    Employee(202, "Diya Sharma", "Sr. Manager", 18.0, 64, 130.0),
    Employee(203, "Reyansh Kumar", "Manager", 14.0, 48, 105.0),
    Employee(204, "Ananya Reddy", "Tech Lead", 12.0, 42, 90.0),
    Employee(205, "Vihaan Singh", "Sr. Engineer", 9.0, 30, 70.0),
    Employee(206, "Saanvi Iyer", "Data Analyst", 7.5, 26, 58.0),
    Employee(207, "Arjun Nair", "Associate", 4.5, 12, 35.0),
    Employee(208, "Ishani Desai", "Jr. Developer", 4.0, 12, 32.0),
    Employee(209, "Karan Mehta", "Intern", 2.0, 6, 15.0),
    Employee(210, "Pari Joshi", "Trainee", 2.5, 3, 20.0),
]

print(f"=== {Employee.company_name} Compensation Audit Summary ===")
print("-" * 85)
for emp in employees_list:
    emp.display_details()





