import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
