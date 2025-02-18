import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
