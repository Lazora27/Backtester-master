import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und WilliamsR
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'WilliamsR': 1.0
        })
    )
