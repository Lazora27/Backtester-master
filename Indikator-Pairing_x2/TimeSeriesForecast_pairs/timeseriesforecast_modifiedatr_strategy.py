import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'ModifiedATR': 1.0
        })
    )
