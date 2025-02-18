import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_AwesomeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und AwesomeOscillator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'AwesomeOscillator': 1.0
        })
    )
