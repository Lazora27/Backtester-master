import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
