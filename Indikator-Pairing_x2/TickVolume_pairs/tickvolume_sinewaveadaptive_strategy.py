import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
