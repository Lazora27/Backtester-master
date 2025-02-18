import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und WilliamsR
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'WilliamsR': 1.0
        })
    )
