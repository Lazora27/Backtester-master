import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'ExtensionProjections': 1.0
        })
    )
