import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
