import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
