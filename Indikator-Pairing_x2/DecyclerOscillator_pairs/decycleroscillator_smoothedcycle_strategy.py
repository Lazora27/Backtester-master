import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DecyclerOscillator_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DecyclerOscillator und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'DecyclerOscillator': 1.0,
            'SmoothedCycle': 1.0
        })
    )
