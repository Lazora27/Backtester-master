import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
