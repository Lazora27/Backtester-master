import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
