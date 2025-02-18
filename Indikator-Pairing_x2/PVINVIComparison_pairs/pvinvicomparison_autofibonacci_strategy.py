import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'AutoFibonacci': 1.0
        })
    )
