import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'AverageLogRange': 1.0
        })
    )
