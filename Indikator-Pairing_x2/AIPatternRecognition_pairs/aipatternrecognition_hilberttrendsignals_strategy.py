import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
