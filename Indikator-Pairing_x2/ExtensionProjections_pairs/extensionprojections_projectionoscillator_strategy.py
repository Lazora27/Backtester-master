import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
