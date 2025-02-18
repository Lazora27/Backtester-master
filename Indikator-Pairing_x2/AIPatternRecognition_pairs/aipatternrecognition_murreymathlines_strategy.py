import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'MurreyMathLines': 1.0
        })
    )
