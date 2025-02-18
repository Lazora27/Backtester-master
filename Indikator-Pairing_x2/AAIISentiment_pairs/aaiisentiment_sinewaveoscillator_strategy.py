import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
