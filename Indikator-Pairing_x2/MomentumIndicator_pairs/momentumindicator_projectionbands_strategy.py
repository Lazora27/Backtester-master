import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'ProjectionBands': 1.0
        })
    )
