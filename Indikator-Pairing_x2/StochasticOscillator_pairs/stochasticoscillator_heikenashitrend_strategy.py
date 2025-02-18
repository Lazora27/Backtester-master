import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
