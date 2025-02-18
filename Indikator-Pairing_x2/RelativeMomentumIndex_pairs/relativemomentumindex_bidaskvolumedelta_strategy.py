import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
