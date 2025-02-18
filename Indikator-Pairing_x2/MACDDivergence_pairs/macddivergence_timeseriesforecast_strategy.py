import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
