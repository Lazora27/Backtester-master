import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
