import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
