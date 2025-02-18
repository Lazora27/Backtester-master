import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_HighLowDifference_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und HighLowDifference
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'HighLowDifference': 1.0
        })
    )
