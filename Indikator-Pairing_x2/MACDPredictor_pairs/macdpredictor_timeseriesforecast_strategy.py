import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
