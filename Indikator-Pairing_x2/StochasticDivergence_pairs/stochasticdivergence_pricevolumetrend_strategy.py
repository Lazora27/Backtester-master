import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
