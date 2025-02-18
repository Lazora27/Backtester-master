import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'WeeklyCycle': 1.0
        })
    )
