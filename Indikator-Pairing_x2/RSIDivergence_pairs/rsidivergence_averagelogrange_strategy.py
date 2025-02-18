import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AverageLogRange': 1.0
        })
    )
