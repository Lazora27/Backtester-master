import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'MarketBalance': 1.0
        })
    )
