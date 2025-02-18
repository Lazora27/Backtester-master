import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
