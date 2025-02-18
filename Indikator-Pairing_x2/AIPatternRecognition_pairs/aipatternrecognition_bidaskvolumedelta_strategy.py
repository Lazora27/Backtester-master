import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
