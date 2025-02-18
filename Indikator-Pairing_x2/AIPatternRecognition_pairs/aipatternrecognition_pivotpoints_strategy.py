import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und PivotPoints
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'PivotPoints': 1.0
        })
    )
