import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'ProjectionBands': 1.0
        })
    )
