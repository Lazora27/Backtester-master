import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'FlowOfFunds': 1.0
        })
    )
