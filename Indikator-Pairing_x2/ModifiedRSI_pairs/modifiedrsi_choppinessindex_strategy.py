import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
