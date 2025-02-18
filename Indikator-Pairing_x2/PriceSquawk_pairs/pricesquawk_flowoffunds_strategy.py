import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'FlowOfFunds': 1.0
        })
    )
