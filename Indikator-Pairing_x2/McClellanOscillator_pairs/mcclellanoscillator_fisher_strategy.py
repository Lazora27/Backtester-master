import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und Fisher
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'Fisher': 1.0
        })
    )
