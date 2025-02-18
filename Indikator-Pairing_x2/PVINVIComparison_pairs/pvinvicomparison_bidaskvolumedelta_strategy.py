import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
