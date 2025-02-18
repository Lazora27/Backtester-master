import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'PutCallRatio': 1.0
        })
    )
