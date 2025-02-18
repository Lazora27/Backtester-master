import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und MarketBalance
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'MarketBalance': 1.0
        })
    )
