import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
