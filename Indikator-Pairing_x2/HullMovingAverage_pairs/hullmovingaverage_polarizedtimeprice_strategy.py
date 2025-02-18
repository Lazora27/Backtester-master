import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
