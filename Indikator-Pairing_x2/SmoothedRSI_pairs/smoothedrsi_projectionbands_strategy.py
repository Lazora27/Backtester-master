import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'ProjectionBands': 1.0
        })
    )
