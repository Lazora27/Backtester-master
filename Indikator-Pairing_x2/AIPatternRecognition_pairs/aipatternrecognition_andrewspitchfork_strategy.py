import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
