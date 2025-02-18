import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
