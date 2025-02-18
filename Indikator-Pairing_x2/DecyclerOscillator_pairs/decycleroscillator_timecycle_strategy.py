import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DecyclerOscillator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DecyclerOscillator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'DecyclerOscillator': 1.0,
            'TimeCycle': 1.0
        })
    )
