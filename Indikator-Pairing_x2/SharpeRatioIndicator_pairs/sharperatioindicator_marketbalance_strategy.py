import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'MarketBalance': 1.0
        })
    )
