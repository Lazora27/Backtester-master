import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
