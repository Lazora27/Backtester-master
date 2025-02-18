import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
