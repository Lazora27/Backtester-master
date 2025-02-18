import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'FlowOfFunds': 1.0
        })
    )
