import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'DonchianChannels': 1.0
        })
    )
