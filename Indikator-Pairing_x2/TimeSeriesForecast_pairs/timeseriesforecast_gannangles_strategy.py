import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und GannAngles
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'GannAngles': 1.0
        })
    )
