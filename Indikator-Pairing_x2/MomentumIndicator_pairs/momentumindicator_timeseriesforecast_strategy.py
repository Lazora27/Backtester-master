import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
