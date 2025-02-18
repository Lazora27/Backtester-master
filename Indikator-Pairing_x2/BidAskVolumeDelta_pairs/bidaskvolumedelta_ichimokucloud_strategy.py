import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'IchimokuCloud': 1.0
        })
    )
