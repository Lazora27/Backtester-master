import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
