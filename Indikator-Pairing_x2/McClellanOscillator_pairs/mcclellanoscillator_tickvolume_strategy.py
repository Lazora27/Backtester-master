import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und TickVolume
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'TickVolume': 1.0
        })
    )
