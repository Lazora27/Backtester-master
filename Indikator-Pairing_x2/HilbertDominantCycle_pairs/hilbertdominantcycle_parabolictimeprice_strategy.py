import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
