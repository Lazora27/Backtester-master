import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'ProjectionBands': 1.0
        })
    )
