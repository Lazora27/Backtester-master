import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'ModifiedATR': 1.0
        })
    )
