import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
