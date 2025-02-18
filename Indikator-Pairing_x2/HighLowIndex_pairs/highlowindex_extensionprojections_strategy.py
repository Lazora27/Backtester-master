import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'ExtensionProjections': 1.0
        })
    )
