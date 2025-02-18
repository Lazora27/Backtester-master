import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und MassIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'MassIndex': 1.0
        })
    )
