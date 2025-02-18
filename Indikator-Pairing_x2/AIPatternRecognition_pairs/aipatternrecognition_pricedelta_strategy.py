import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und PriceDelta
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'PriceDelta': 1.0
        })
    )
