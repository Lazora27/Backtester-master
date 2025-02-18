import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
