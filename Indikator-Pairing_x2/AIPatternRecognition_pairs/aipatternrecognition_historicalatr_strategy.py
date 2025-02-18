import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'HistoricalATR': 1.0
        })
    )
