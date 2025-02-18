import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
