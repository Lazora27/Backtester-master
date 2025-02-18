import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_ArmsIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und ArmsIndex
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'ArmsIndex': 1.0
        })
    )
