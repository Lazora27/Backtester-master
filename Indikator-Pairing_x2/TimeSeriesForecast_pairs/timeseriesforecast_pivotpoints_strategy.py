import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und PivotPoints
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'PivotPoints': 1.0
        })
    )
