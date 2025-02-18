import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
