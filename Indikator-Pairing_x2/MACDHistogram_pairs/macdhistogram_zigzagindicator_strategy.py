import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
