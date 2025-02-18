import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'ModifiedRSI': 1.0
        })
    )
