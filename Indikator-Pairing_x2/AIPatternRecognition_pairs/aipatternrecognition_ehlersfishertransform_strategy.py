import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
