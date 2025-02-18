import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
