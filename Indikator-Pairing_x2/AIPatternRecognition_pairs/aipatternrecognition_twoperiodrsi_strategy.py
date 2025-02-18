import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
