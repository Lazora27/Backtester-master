import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
