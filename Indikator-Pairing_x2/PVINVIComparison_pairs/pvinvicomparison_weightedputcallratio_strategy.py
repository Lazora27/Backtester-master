import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
