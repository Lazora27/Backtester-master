import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und CCITurbo
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'CCITurbo': 1.0
        })
    )
