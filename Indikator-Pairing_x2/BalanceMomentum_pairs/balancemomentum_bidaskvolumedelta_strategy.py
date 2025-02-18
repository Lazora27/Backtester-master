import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
