import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ExtensionProjections': 1.0
        })
    )
