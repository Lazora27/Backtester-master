import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_ChaikinMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und ChaikinMoneyFlow
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'ChaikinMoneyFlow': {
                'class': ChaikinMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinMoneyFlow'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'ChaikinMoneyFlow': 1.0
        })
    )
