import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
