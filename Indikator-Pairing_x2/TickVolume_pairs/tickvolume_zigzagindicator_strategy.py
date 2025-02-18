import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
