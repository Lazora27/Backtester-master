import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
