import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
