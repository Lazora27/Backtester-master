import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'ParabolicSAR': 1.0
        })
    )
