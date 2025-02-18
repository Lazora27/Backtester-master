import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
