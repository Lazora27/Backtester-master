import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'SmoothedCycle': 1.0
        })
    )
