import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'PriceSquawk': 1.0
        })
    )
