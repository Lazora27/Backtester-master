import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'VolumeDelta': 1.0
        })
    )
