import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_MLForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und MLForecast
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'MLForecast': 1.0
        })
    )
