import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'VolumeOscillator': 1.0
        })
    )
