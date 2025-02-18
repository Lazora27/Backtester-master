import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
