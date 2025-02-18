import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und Fisher
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'Fisher': 1.0
        })
    )
