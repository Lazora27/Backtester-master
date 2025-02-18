import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_AdvanceDeclineLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und AdvanceDeclineLine
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'AdvanceDeclineLine': 1.0
        })
    )
