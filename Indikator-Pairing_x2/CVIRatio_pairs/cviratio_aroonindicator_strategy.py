import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'AroonIndicator': 1.0
        })
    )
