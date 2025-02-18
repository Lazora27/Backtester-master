import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'ProjectionBands': 1.0
        })
    )
