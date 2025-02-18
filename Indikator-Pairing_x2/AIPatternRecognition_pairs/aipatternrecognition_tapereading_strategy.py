import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und TapeReading
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'TapeReading': 1.0
        })
    )
