import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'MACDPredictor': 1.0
        })
    )
