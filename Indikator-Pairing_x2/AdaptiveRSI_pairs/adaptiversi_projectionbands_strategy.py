import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'ProjectionBands': 1.0
        })
    )
