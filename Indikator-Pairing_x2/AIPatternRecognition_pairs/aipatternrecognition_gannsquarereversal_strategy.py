import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'GannSquareReversal': 1.0
        })
    )
