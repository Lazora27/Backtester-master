import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'HilbertTrendline': 1.0
        })
    )
