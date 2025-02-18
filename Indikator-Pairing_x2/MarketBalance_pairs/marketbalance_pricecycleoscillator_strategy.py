import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
