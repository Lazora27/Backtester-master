import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und CyberCycle
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'CyberCycle': 1.0
        })
    )
