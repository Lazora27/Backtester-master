import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
