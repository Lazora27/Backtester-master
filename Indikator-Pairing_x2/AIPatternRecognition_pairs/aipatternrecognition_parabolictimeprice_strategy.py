import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
