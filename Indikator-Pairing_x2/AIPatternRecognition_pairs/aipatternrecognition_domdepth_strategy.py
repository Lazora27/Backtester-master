import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und DOMDepth
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'DOMDepth': 1.0
        })
    )
