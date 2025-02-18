import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'CumulativeTick': 1.0
        })
    )
