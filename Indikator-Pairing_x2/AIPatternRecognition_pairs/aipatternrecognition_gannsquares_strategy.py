import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und GannSquares
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'GannSquares': 1.0
        })
    )
