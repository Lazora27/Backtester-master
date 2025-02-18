import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und MassIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'MassIndex': 1.0
        })
    )
