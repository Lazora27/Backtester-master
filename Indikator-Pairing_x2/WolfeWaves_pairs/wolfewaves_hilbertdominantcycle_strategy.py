import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
