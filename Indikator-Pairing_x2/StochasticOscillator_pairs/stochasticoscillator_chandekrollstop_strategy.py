import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
