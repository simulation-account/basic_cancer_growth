
from cc3d import CompuCellSetup
        

from basic_cancer_growthSteppables import CellLayoutSteppable
CompuCellSetup.register_steppable(steppable=CellLayoutSteppable(frequency=1))


from basic_cancer_growthSteppables import ConstraintInitializerSteppable
CompuCellSetup.register_steppable(steppable=ConstraintInitializerSteppable(frequency=1))




from basic_cancer_growthSteppables import GrowthSteppable
CompuCellSetup.register_steppable(steppable=GrowthSteppable(frequency=1))




from basic_cancer_growthSteppables import MitosisSteppable
CompuCellSetup.register_steppable(steppable=MitosisSteppable(frequency=1))




from basic_cancer_growthSteppables import DeathSteppable
CompuCellSetup.register_steppable(steppable=DeathSteppable(frequency=1))


CompuCellSetup.run()