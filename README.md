# fungal_metagenomics_ITS_coverage_calculator
I coded this function to estimate the fraction of the ITS predictions from the fungal metagenomics and it estimates by taking into account the sequence length and also the ITS1 and ITS2 start and stop coordinates. Provided a keyworded argument, it estimates the coverage accordingly. 

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
 'FJ554459_uncultured_': 20.17075773745998}
