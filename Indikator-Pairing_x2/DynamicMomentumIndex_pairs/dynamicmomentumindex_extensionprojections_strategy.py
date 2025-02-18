import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'ExtensionProjections': 1.0
        })
    )
