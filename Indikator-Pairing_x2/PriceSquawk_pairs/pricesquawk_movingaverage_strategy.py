import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und MovingAverage
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'MovingAverage': 1.0
        })
    )
