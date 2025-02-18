import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und SuperMACD
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'SuperMACD': 1.0
        })
    )
