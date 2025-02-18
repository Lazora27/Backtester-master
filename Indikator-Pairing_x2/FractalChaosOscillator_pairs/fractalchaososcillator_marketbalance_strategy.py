import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'MarketBalance': 1.0
        })
    )
