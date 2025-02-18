import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'DonchianChannels': 1.0
        })
    )
