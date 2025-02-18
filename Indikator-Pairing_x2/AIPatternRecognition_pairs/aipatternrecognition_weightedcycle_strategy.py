import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'WeightedCycle': 1.0
        })
    )
