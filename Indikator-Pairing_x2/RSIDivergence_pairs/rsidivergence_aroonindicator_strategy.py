import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AroonIndicator': 1.0
        })
    )
