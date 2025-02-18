import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_PVINVIComparison_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und PVINVIComparison
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'PVINVIComparison': 1.0
        })
    )
