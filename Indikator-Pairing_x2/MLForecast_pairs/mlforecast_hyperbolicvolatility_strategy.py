import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
