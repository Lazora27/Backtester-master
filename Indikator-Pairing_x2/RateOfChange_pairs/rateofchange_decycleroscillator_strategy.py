import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
