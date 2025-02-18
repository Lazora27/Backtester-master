import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
