import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
