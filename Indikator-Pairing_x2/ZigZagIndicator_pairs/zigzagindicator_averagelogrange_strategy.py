import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'AverageLogRange': 1.0
        })
    )
