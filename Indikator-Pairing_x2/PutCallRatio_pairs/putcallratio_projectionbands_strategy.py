import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ProjectionBands': 1.0
        })
    )
