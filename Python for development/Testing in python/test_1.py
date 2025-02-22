import unittest
from unittest.mock import patch
from q import FermosaExtracter


class TestFermosa(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Testing is started")
    
    @classmethod
    def tearDownClass(cls):
        print("Testing is completed")

    def setUp(self):
        self.ansdict=[{"test":1},{"test2":2}]
        outputname="testfile.xlsx"
        self.testobj=FermosaExtracter("",9,outputname)
  

    def tearDown(self):
        pass

    def test_core(self):
        pass

    def test_makedata(self):
        with patch("requests.get") as mocker:
            mocker.return_value.text="<div class='pd_summary'><p>Hello</p></div>"
            link="https://www.combo.com"
            type="combo"
            name="ram"
            price=9000
            varigated="Not Valid"
            self.assertEqual(self.testobj._FermosaExtracter__makeData(link,type,name,price,varigated),{"Link":link,
                              "Price":price,
                              "Type":type,
                              "Name":name,
                              "Variegated":varigated})
            mocker.assert_called_once_with(link)
            

    def test_savedata(self):
        with patch("pandas.DataFrame.to_excel") as mocker:
            mocker.return_value=True
            self.ansdict=[{"test":1},{"test2":2}]
            outputname="testfile.xlsx"
            self.testobj.saveData()
            mocker.assert_called_once_with(outputname,index=False,engine='openpyxl')
            

        with patch("pandas.DataFrame.to_excel") as mocker, patch("builtins.print") as pr:
            mocker.side_effect= Exception("")
            self.testobj.saveData()
            pr.assert_called_once_with("Error during saving the data in excel ")



if __name__=="__main__":
    unittest.main()



