import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und MarketBalance
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'MarketBalance': 1.0
        })
    )
