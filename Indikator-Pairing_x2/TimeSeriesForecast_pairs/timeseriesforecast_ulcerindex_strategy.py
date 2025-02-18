import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'UlcerIndex': 1.0
        })
    )
