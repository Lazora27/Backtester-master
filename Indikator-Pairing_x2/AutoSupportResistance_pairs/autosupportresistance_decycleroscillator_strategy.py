import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
