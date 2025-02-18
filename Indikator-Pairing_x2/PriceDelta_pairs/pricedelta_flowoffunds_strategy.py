import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'FlowOfFunds': 1.0
        })
    )
