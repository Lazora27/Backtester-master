import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'KeltnerChannels': 1.0
        })
    )
