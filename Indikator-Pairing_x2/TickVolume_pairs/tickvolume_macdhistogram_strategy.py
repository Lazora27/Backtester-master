import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'MACDHistogram': 1.0
        })
    )
