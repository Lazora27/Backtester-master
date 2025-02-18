import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
