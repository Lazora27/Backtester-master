import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
