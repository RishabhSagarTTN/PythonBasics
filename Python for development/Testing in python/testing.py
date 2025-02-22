import unittest
from unittest.mock import patch, MagicMock
import requests
import pandas as pd
from io import BytesIO

# Assuming FermosaExtracter class is already imported above

class TestFermosaExtracter(unittest.TestCase):

    def setUp(self):
        """Create an instance of FermosaExtracter for testing"""
        self.extracter = FermosaExtracter("https://fermosaplants.com/collections/sansevieria", 2, "test_output.xlsx")
        
    @patch('requests.get')
    def test_makeData(self, mock_get):
        """Test the __makeData method"""
        # Mocking the response for the page
        mock_response = MagicMock()
        mock_response.text = """
        <div class="pd_summary">
            <p>1. Image Description: beautiful combo plant. Images: Image 1, Image 2, Image 3</p>
        </div>
        """
        mock_get.return_value = mock_response

        # Test input data for the function
        link = "https://fermosaplants.com/some-plant"
        type_ = "combo"
        name = "Beautiful Combo Plant"
        price = "$30"
        varigated = "Variegated"
        
        expected_dict = {
            "Link": link,
            "Price": price,
            "Type": type_,
            "Name": name,
            "Variegated": varigated,
            "Name1": "beautiful combo plant"
        }

        result = self.extracter._FermosaExtracter__makeData(link, type_, name, price, varigated)
        self.assertEqual(result, expected_dict)

    @patch('requests.get')
    def test_core_method(self, mock_get):
        """Test the __core method"""
        # Mocking the data returned by the site
        mock_response = MagicMock()
        mock_response.text = """
        <div class="product-item-v5">
            <div>
                <h4><a href="/some-plant">Beautiful Combo Plant</a></h4>
                <p class="price-product mb-0"><span>$30</span></p>
            </div>
        </div>
        """
        mock_get.return_value = mock_response
        
        # Simulate one page of data extraction
        self.extracter.__core()
        
        # Verify the result stored in ansdict
        self.assertEqual(len(self.extracter.ansdict), 1)
        self.assertEqual(self.extracter.ansdict[0]["Name"], "Beautiful Combo Plant")
        self.assertEqual(self.extracter.ansdict[0]["Price"], "$30")

    @patch('pandas.DataFrame.to_excel')
    def test_saveData(self, mock_to_excel):
        """Test the saveData method"""
        # Sample data to save
        self.extracter.ansdict = [{"Link": "https://fermosaplants.com/some-plant", "Name": "Beautiful Combo Plant", "Price": "$30"}]
        
        # Run saveData
        self.extracter.saveData()
        
        # Assert that to_excel method was called once
        mock_to_excel.assert_called_once()

    @patch('requests.get')
    def test_full_process(self, mock_get):
        """Test the entire process from start to save"""
        # Mocking data for the core method
        mock_response = MagicMock()
        mock_response.text = """
        <div class="product-item-v5">
            <div>
                <h4><a href="/some-plant">Beautiful Combo Plant</a></h4>
                <p class="price-product mb-0"><span>$30</span></p>
            </div>
        </div>
        """
        mock_get.return_value = mock_response

        # Patch pandas to avoid actual file writing
        with patch('pandas.DataFrame.to_excel') as mock_to_excel:
            # Run the full process
            self.extracter.startProcess()

            # Verify if the process completed successfully
            self.assertEqual(len(self.extracter.ansdict), 1)
            mock_to_excel.assert_called_once()

if __name__ == '__main__':
    unittest.main()
