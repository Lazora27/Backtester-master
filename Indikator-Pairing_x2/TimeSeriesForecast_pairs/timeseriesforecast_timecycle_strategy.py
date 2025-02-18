import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und TimeCycle
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'TimeCycle': 1.0
        })
    )
