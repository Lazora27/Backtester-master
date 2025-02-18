import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'VolatilityIndex': 1.0
        })
    )
