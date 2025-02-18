import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
