from dateien.pdf import pdf_ready
import os
import shutil



def test_pdf_function():
    # Erstelle temporären Ordner
    test_dir = os.path.join(os.getcwd(), "test_dir")
    os.makedirs(test_dir)

    # Erstelle einige Test-PDF-Dateien
    pdf_files = ["test1.pdf", "test2.pdf", "test3.pdf"]
    for file in pdf_files:
        with open(os.path.join(test_dir, file), "w") as f:
            f.write("Test PDF content")

    # Rufe die pdf()-Funktion mit dem temporären Ordnerpfad auf
    pdf_ready(test_dir)

    # Überprüfe, ob die PDF-Dateien erfolgreich in den Zielordner verschoben wurden
    expected_dir = os.path.join(test_dir, "PDF")
    assert os.path.exists(expected_dir)

    for file in pdf_files:
        expected_path = os.path.join(expected_dir, file)
        assert os.path.exists(expected_path)

    # Lösche den temporären Ordner
    shutil.rmtree(test_dir)
