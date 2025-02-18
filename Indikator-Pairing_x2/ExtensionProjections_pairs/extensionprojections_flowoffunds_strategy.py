import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'FlowOfFunds': 1.0
        })
    )
