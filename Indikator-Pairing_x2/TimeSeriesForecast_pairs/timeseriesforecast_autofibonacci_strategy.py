import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'AutoFibonacci': 1.0
        })
    )
