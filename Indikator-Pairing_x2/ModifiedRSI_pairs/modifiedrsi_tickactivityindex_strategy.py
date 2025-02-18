import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'TickActivityIndex': 1.0
        })
    )
