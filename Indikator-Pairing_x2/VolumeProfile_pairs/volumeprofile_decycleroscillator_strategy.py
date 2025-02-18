import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
