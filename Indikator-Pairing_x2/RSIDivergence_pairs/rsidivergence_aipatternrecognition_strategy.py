import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AIPatternRecognition_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AIPatternRecognition
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AIPatternRecognition': 1.0
        })
    )
