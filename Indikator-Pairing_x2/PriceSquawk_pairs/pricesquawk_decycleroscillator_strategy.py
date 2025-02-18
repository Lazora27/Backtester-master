import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
