import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ProjectionBands': 1.0
        })
    )
