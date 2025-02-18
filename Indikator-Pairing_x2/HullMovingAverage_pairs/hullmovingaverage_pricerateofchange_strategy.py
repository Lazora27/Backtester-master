import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
