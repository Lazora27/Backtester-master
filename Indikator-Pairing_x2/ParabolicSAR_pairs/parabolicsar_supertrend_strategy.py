import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und SuperTrend
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'SuperTrend': 1.0
        })
    )
