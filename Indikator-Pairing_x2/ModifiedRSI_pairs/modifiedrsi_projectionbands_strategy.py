import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'ProjectionBands': 1.0
        })
    )
