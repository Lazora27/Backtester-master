import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'TrendCycles': 1.0
        })
    )
