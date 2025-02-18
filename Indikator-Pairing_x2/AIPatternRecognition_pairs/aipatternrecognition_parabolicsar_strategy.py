import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'ParabolicSAR': 1.0
        })
    )
