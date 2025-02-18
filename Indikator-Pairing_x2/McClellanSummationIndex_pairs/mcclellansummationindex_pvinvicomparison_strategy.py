import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_PVINVIComparison_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und PVINVIComparison
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'PVINVIComparison': 1.0
        })
    )
