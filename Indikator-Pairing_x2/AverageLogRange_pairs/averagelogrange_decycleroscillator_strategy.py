import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
