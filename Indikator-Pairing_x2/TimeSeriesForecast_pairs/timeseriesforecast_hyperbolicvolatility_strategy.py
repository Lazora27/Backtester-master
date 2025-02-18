import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
