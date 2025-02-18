import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'ExtensionProjections': 1.0
        })
    )
