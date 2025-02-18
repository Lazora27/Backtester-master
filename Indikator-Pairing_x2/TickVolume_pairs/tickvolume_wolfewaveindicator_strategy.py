import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
