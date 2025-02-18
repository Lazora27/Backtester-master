import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'PutCallRatio': 1.0
        })
    )
