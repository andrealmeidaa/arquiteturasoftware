class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        return f"Report: {self.data}"

class PDFExporter:
    def export(self, report):
        print(f"Exportando {report.generate_report()} para PDF")

class CSVExporter:
    def export(self, report):
        print(f"Exportando {report.generate_report()} para CSV")

class JSONExporter:
    def export(self, report):
        print(f"Exportando {report.generate_report()} para JSON")

if __name__=="__main__":
    report=Report("Dados Ok")
    print(report.generate_report())
    pdfExporter=PDFExporter()
    pdfExporter.export(report=report)
    csvExporter=CSVExporter()
    csvExporter.export(report=report)
    jsonExporter=JSONExporter()
    jsonExporter.export(report=report)