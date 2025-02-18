import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_PVINVIComparison_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und PVINVIComparison
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'PVINVIComparison': 1.0
        })
    )
