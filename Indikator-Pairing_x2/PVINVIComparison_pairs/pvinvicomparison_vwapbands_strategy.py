import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und VWAPBands
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'VWAPBands': 1.0
        })
    )
