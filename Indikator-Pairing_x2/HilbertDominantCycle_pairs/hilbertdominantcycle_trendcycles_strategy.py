import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und TrendCycles
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'TrendCycles': 1.0
        })
    )
