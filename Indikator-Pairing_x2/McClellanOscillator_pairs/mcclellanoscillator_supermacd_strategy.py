import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und SuperMACD
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'SuperMACD': 1.0
        })
    )
