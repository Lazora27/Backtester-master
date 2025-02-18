import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'ConnorsRSI': 1.0
        })
    )
