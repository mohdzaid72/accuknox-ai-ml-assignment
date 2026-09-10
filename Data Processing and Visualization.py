import requests
import matplotlib.pyplot as plt


class StudentAnalyzer:

    API_URL = "https://api.slingacademy.com/v1/sample-data/files/student-scores.json"

    SCORE_FIELDS = [
        "math_score",
        "history_score",
        "physics_score",
        "chemistry_score",
        "biology_score",
        "english_score",
        "geography_score"
    ]

    def __init__(self):
        self.students = []
        self.names = []
        self.averages = []

    def fetch_students(self):
       
        response = requests.get(self.API_URL, timeout=10)
        response.raise_for_status()

        self.students = response.json()

        print("Students fetched:", len(self.students))

    def calculate_averages(self):
        for student in self.students:
            scores = [
                student[field]
                for field in self.SCORE_FIELDS
                if isinstance(student.get(field), (int, float))
            ]

            if scores:
                average = sum(scores) / len(scores)

                name = f"{student['first_name']} {student['last_name']}"

                self.names.append(name)
                self.averages.append(average)

                print(f"{name}: {average:.2f}")

    def calculate_overall_average(self):
        if not self.averages:
            print("No valid student scores found.")
            return

        overall_average = sum(self.averages) / len(self.averages)

        print(f"\nOverall Average: {overall_average:.2f}")

    def create_chart(self):
        plt.figure(figsize=(14, 7))

        plt.bar(self.names, self.averages)

        plt.xlabel("Students")
        plt.ylabel("Average Score")
        plt.title("Student Average Test Scores")

        plt.xticks(rotation=45, ha="right")
        plt.ylim(0, 100)

        plt.tight_layout()

        plt.savefig("student_scores.png", dpi=300)

        print("\nChart saved successfully as student_scores.png")

        plt.show()

    def run(self):
        self.fetch_students()
        self.calculate_averages()
        self.calculate_overall_average()
        self.create_chart()



analyzer = StudentAnalyzer()
analyzer.run()
