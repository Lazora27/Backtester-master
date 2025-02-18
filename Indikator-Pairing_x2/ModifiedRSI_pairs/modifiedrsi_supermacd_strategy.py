import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und SuperMACD
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'SuperMACD': 1.0
        })
    )
