import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'TimeCycle': 1.0
        })
    )
