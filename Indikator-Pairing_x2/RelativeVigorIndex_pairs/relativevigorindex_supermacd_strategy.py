import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und SuperMACD
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'SuperMACD': 1.0
        })
    )
