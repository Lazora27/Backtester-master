import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'ProjectionBands': 1.0
        })
    )
