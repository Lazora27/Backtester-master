import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
