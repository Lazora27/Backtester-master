import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
