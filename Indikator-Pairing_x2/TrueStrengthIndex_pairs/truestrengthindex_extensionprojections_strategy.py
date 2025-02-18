import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'ExtensionProjections': 1.0
        })
    )
