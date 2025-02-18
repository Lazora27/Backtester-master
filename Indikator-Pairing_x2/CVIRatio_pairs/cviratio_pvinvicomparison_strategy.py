import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_PVINVIComparison_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und PVINVIComparison
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'PVINVIComparison': 1.0
        })
    )
