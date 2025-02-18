import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
