import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'KeltnerChannels': 1.0
        })
    )
