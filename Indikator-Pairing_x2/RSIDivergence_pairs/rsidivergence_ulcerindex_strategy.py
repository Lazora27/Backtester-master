import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'UlcerIndex': 1.0
        })
    )
