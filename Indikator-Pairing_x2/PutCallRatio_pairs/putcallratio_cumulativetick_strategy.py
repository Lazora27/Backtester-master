import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'CumulativeTick': 1.0
        })
    )
