import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
