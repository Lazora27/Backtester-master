import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
