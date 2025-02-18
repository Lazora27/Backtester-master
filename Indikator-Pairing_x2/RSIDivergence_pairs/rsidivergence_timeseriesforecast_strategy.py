import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
