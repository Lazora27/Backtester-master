import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'BuyingPressure': 1.0
        })
    )
