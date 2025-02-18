import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'MarketBalance': 1.0
        })
    )
