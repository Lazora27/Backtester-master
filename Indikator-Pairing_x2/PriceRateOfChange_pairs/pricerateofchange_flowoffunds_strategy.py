import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'FlowOfFunds': 1.0
        })
    )
