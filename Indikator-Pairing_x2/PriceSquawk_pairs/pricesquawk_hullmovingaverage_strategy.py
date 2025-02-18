import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'HullMovingAverage': 1.0
        })
    )
