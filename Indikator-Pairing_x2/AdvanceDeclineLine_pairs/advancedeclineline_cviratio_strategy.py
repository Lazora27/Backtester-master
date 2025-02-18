import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_CVIRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und CVIRatio
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'CVIRatio': 1.0
        })
    )
