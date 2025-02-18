import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'SmoothedRSI': 1.0
        })
    )
