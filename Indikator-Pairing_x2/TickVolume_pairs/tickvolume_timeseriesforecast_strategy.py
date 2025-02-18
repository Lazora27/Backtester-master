import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
