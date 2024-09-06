class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        return f"Report: {self.data}"

    def export_to_pdf(self):
        print(f"Exportando {self.data} para PDF")

    def export_to_csv(self):
        print(f"Exportando {self.data} para CSV")

if __name__=="__main__":
    report=Report("Dados Ok")
    print(report.generate_report())
    report.export_to_pdf()
    report.export_to_csv()