import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
