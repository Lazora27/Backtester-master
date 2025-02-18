import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
