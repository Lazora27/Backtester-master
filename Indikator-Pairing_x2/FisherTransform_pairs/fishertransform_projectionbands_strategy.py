import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'ProjectionBands': 1.0
        })
    )
