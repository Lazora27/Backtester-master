import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ArnaudLegouxMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ArnaudLegouxMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ArnaudLegouxMovingAverage': {
                'class': ArnaudLegouxMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArnaudLegouxMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ArnaudLegouxMovingAverage': 1.0
        })
    )
