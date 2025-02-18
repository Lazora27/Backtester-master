import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'HilbertTrendline': 1.0
        })
    )
