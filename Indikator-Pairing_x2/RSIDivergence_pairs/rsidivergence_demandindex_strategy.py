import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und DemandIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'DemandIndex': 1.0
        })
    )
