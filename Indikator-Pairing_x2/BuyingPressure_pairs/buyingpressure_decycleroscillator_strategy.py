import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
