import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'AverageTrueRange': 1.0
        })
    )
