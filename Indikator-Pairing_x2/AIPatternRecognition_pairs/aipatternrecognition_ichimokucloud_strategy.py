import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'IchimokuCloud': 1.0
        })
    )
