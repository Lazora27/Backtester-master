import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_CVIRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und CVIRatio
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'CVIRatio': 1.0
        })
    )
