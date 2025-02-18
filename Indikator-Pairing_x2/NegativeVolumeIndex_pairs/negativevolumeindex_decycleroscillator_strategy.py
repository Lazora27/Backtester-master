import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
