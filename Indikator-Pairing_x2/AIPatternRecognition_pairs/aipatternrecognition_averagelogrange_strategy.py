import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'AverageLogRange': 1.0
        })
    )
