import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
