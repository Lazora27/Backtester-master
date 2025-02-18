import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und CycleFinder
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'CycleFinder': 1.0
        })
    )
