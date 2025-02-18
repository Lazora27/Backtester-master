import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
