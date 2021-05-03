# Instructions :
# This challenge is about Biology.

# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.

# A Gene is a single value 0 or 1, it can mutate (flip).
class Gene():
    def __init__(self,value):
        self.value=value
    
    def mutate(self):
        if self.value==1:
            self.value=0
        else:
            self.value=1
# A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
class Chromosome():
    def __init__(self,gene_series):
        self.gene_series=gene_series
    
# A DNA is a series of 10 chromosome, and it can also mutate the same way Chromosomes can.
# Implement these classes as you see fit.
class DNA():
    def __init__(self,chromosome_series):
        self.chromosome_series=chromosome_series
# Create a new class called Organism that accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate.
class Organism():
    def __init__(self,dna_object,environment):
        
# Instantiate a number of Organims and let them mutate until one gets to a DNA is only made of 1s. Then stop and record the number of generations (iterations) it took.