import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
