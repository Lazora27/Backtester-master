import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
