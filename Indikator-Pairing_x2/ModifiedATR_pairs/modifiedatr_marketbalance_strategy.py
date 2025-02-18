import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'MarketBalance': 1.0
        })
    )
