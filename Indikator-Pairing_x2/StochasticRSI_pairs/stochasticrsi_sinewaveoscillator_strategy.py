import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
