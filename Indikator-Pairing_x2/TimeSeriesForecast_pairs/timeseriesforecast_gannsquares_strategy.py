import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und GannSquares
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'GannSquares': 1.0
        })
    )
