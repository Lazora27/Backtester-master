import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'MACDHistogram': 1.0
        })
    )
