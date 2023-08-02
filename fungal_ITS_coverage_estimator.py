def fungalMetagenomicsCoverageCalculator(its_file, its_type = None):
    """
    _summary_
    a fungal metagenomics ITS prediction coverage calculator,
    given an ITS prediction output file from the ITSx predictor,
    it will estimate the coverage of the ITS predictions, it estimates
    the fungal metagenomics ITS coverage by taking into account the start
    of the ITS1 and end of the ITS1 and the sequence length from which the
    ITS is predicted. It does the same for the ITS2. 
    Arguments:
        its_file -- _description_
        its prediction file
    Keyword Arguments:
        its_type -- _description_ (default: {None})
        whether you want the its1 or its2
    Returns:
        _description_
        a flat list containing the sequence name and the fungalmetagenomics
        coverage.
    """
    its1_start = list(map(int,pd.read_csv(its_file, sep = "\t").\
                                        iloc[::,[0,5]].dropna().iloc[::,1].\
                                                apply(lambda n: n.split(":")[1]).\
                                                        apply(lambda n: n.split("-")[0])))
    its1_end = list(map(int,pd.read_csv(its_file, sep = "\t").\
                                        iloc[::,[0,5]].dropna().iloc[::,1].\
                                                apply(lambda n: n.split(":")[1]).\
                                                        apply(lambda n: n.split("-")[1])))
    its2_start = list(map(int,pd.read_csv(its_file, sep = "\t").\
                                        iloc[::,[0,6]].dropna().iloc[::,1].\
                                                apply(lambda n: n.split(":")[1]).\
                                                        apply(lambda n: n.split("-")[0])))                  
    its2_end = list(map(int,pd.read_csv(its_file, sep = "\t"). \
                                        iloc[::,[0,6]].dropna().iloc[::,1]. \
                                                apply(lambda n: n.split(":")[1]). \
                                                        apply(lambda n: n.split("-")[1])))  
    its1_names = pd.read_csv(its_file, sep = "\t").\
                                        iloc[::,[0,5]].dropna().iloc[::,0].\
                                                apply(lambda n: n.split(" ")[3].\
                                                        replace("...", "")).to_list() 
    its2_names = pd.read_csv(its_file, sep = "\t").\
                                        iloc[::,[0,6]].dropna().iloc[::,0].\
                                                apply(lambda n: n.split(" ")[3].\
                                                        replace("...", "")).to_list()
    seq_length_its1 = list(map(int,pd.read_csv(its_file, sep = "\t").\
                                        iloc[::,[0,5]].dropna().iloc[::,0].\
                                                apply(lambda n: n.split(" ")[4]).to_list()))
    seq_length_its2 = list(map(int,pd.read_csv(its_file, sep = "\t").\
                                        iloc[::,[0,6]].dropna().iloc[::,0].
                                                apply(lambda n: n.split(" ")[4]).to_list()))
    if its_type == "its1":
        its1_coverage = {}
        for i in range(len(its1_start)):
            its1_coverage[its1_names[i]] = \
                    ((its1_end[i] - its1_start[i])/seq_length_its1[i])*100
        return its1_coverage
    elif its_type == "its2":
        its2_coverage = {}
        for i in range(len(its2_start)):
            its2_coverage[its2_names[i]] = \
                    ((its2_end[i] - its2_start[i])/seq_length_its2[i])*100
        return its2_coverage            
    else:
         print("No type specified")                                                                                                        
