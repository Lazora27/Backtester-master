import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
