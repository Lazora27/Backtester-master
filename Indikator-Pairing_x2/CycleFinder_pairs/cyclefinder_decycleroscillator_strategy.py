import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
