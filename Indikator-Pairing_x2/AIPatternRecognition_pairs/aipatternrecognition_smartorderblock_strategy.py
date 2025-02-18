import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_SmartOrderBlock_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und SmartOrderBlock
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'SmartOrderBlock': 1.0
        })
    )
