import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_PVINVIComparison_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und PVINVIComparison
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'PVINVIComparison': 1.0
        })
    )
