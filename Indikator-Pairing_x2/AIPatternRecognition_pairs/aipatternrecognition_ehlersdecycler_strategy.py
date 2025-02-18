import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'EhlersDecycler': 1.0
        })
    )
