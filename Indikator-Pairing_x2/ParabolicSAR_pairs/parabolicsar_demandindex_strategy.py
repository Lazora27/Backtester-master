import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und DemandIndex
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'DemandIndex': 1.0
        })
    )
