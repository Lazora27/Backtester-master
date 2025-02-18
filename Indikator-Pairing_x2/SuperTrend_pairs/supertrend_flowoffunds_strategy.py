import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'FlowOfFunds': 1.0
        })
    )
