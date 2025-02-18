import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'SmoothedRSI': 1.0
        })
    )
