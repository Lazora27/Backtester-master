import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und RateOfChange
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'RateOfChange': 1.0
        })
    )
