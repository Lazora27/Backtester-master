import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'ModifiedATR': 1.0
        })
    )
