import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
