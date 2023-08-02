# fungal_metagenomics_ITS_coverage_calculator
I coded this function to estimate the fraction of the ITS predictions from the fungal metagenomics and it estimates by taking into account the sequence length and also the ITS1 and ITS2 start and stop coordinates. Provided a keyworded argument, it estimates the coverage accordingly. This was missing in ITS predictions, so i coded this to enable a plot visualization to see how much your sequence fragement is covered. 

```python 
fungalMetagenomicsCoverageCalculator(its_file = "/Users/gauravsablok/Desktop/CodeCheck/Write/outdata.csv", its_type = "its1")
{'FJ554463_uncultured_': 18.381502890173408, 
 'FJ554462_uncultured_': 18.057022175290392, 
 'FJ554460_uncultured_': 22.540983606557376, 
 'FJ554459_uncultured_': 20.064034151547492}
fungalMetagenomicsCoverageCalculator(its_file = "/Users/gauravsablok/Desktop/CodeCheck/Write/outdata.csv", its_type = "its2")
{'FJ554463_uncultured_': 16.99421965317919, 
 'FJ554462_uncultured_': 22.70327349524815, 
 'FJ554460_uncultured_': 20.184426229508194, 
 'FJ554459_uncultured_': 20.17075773745998}```

Gaurav Sablok \
Senior Postdoctoral Fellow \
Faculty of Natural and Agricultural Sciences Room 7-35, \
Agricultural Sciences Building University of Pretoria, \
Private Bag X20 Hatfield 0028, South Africa \
Academia : https://up-za.academia.edu/GauravSablok \
Frontiers: https://loop.frontiersin.org/people/33293/overview \
ORCID: https://orcid.org/0000-0002-4157-9405 \
WOS: https://www.webofscience.com/wos/author/record/C-5940-2014 \
Github:https://github.com/sablokgaurav \
Linkedin: https://www.linkedin.com/in/sablokgaurav/ \
ResearchGate: https://www.researchgate.net/profile/Gaurav-Sablok \
