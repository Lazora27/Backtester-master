import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
