import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
