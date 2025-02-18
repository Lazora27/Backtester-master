import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
