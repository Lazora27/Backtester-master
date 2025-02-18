import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
