import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'SmoothedCycle': 1.0
        })
    )
