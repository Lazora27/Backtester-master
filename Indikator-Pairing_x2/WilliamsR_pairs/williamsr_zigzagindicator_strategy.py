import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
