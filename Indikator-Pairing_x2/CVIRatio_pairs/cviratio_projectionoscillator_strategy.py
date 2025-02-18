import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
