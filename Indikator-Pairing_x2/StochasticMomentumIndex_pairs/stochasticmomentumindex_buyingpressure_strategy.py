import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
