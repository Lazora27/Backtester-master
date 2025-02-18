import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'ExtensionProjections': 1.0
        })
    )
