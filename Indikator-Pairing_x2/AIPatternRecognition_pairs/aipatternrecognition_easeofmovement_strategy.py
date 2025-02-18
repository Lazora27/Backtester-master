import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'EaseOfMovement': 1.0
        })
    )
