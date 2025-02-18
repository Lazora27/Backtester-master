import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'UltimateOscillator': 1.0
        })
    )
