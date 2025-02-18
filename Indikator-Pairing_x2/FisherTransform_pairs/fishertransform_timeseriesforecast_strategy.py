import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
