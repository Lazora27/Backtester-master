import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
