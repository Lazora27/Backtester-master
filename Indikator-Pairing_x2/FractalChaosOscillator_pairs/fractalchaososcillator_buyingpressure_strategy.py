import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'BuyingPressure': 1.0
        })
    )
