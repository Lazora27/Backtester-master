import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und BarStrength
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'BarStrength': 1.0
        })
    )
