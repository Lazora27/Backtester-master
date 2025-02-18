import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
