import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'ProjectionBands': 1.0
        })
    )
