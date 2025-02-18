import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'CoppockCurve': 1.0
        })
    )
