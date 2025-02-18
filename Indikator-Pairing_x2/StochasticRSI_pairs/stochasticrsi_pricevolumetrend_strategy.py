import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
