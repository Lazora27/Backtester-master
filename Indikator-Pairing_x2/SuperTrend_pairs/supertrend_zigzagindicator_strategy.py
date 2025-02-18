import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
