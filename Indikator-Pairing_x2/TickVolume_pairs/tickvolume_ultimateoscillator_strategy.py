import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'UltimateOscillator': 1.0
        })
    )
