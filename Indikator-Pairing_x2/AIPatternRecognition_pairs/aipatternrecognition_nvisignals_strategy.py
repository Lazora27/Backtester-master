import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_NVISignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und NVISignals
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'NVISignals': 1.0
        })
    )
