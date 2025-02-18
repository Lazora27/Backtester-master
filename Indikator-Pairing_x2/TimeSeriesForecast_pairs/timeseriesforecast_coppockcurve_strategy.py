import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'CoppockCurve': 1.0
        })
    )
