import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'OpenInterest': 1.0
        })
    )
