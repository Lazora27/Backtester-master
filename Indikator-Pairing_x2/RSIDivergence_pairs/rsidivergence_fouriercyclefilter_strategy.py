import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
