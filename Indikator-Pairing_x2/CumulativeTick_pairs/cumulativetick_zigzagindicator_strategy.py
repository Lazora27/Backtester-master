import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
