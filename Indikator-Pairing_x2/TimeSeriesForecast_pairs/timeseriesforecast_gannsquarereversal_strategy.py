import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'GannSquareReversal': 1.0
        })
    )
