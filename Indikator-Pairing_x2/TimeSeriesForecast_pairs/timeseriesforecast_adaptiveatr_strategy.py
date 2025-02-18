import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'AdaptiveATR': 1.0
        })
    )
