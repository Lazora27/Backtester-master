import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'EhlersDecycler': 1.0
        })
    )
