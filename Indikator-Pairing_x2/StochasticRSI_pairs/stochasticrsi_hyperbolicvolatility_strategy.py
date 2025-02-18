import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
