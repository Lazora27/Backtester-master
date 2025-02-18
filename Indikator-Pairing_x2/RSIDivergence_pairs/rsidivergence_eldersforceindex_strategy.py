import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'EldersForceIndex': 1.0
        })
    )
