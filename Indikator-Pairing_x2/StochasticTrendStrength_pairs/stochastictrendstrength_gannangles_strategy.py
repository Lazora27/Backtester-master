import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und GannAngles
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'GannAngles': 1.0
        })
    )
