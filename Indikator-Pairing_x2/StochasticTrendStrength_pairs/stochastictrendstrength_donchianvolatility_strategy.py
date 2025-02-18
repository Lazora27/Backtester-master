import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'DonchianVolatility': 1.0
        })
    )
