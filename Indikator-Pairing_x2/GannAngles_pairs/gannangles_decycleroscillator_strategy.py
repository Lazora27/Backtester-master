import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
