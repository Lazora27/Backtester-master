import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
