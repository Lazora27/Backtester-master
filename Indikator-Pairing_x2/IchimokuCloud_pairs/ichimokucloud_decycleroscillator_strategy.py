import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
