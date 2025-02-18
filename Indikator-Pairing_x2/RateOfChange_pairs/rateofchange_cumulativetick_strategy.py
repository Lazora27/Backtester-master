import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'CumulativeTick': 1.0
        })
    )
