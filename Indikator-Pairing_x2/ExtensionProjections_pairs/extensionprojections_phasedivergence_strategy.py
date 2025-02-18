import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'PhaseDivergence': 1.0
        })
    )
