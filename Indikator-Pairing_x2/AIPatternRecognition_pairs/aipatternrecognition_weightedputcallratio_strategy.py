import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
