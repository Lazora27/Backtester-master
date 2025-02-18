import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
