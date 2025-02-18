import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'CenterOfGravity': 1.0
        })
    )
