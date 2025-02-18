import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'VolumeProfile': 1.0
        })
    )
