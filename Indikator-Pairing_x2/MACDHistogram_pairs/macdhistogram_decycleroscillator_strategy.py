import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
