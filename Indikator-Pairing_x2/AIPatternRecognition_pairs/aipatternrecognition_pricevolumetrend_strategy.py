import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
