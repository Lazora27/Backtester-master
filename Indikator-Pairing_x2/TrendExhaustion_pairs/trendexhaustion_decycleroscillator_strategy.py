import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
