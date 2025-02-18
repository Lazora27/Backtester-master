import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'WolfeWaves': 1.0
        })
    )
