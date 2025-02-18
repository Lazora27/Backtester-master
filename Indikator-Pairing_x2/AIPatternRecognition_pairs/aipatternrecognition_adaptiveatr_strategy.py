import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'AdaptiveATR': 1.0
        })
    )
