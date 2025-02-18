import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
