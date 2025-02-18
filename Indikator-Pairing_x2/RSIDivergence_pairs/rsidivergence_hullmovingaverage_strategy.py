import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'HullMovingAverage': 1.0
        })
    )
