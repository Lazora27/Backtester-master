import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und TapeReading
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'TapeReading': 1.0
        })
    )
