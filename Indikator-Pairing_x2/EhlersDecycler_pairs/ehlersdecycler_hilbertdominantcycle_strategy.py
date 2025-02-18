import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
