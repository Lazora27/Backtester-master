import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'BradleySiderograph': 1.0
        })
    )
