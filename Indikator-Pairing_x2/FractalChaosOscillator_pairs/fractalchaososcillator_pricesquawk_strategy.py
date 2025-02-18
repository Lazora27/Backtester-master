import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'PriceSquawk': 1.0
        })
    )
