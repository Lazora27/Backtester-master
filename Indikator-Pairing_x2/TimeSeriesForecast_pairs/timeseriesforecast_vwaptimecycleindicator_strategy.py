import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_VWAPTimeCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und VWAPTimeCycleIndicator
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'VWAPTimeCycleIndicator': {
                'class': VWAPTimeCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPTimeCycleIndicator'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'VWAPTimeCycleIndicator': 1.0
        })
    )
