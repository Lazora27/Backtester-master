import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
