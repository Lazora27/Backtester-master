import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
