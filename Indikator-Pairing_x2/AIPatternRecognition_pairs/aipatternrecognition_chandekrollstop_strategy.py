import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
