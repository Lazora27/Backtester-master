import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'DonchianVolatility': 1.0
        })
    )
