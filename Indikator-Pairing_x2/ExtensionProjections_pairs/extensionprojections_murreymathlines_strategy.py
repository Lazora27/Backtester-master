import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'MurreyMathLines': 1.0
        })
    )
