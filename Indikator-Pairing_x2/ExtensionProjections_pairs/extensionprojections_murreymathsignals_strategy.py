import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
