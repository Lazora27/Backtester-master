import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
