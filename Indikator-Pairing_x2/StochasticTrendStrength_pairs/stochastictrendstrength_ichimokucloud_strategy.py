import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'IchimokuCloud': 1.0
        })
    )
