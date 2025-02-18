import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
