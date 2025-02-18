import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'SmoothedRSI': 1.0
        })
    )
