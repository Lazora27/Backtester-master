import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
