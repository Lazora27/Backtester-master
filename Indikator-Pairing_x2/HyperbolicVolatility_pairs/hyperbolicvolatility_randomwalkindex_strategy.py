import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
