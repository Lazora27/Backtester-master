import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
