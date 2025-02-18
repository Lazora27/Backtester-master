import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
