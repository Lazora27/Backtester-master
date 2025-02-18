import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'WolfeWaves': 1.0
        })
    )
