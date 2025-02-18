import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
