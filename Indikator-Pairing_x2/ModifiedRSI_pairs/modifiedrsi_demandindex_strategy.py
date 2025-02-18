import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und DemandIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'DemandIndex': 1.0
        })
    )
