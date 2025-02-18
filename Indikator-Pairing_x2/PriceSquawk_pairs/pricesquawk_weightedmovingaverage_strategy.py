import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
