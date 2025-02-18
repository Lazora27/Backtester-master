import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
