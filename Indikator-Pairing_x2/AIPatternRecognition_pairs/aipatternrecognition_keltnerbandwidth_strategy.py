import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
