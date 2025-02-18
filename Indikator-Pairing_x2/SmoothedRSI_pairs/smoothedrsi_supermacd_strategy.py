import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und SuperMACD
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'SuperMACD': 1.0
        })
    )
