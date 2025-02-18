import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
