import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
