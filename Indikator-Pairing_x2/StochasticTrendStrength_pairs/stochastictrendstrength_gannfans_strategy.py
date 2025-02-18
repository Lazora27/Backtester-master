import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und GannFans
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'GannFans': 1.0
        })
    )
