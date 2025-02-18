import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TimeCycle
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TimeCycle': 1.0
        })
    )
