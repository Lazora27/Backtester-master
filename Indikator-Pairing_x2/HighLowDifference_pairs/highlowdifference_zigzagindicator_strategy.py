import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
