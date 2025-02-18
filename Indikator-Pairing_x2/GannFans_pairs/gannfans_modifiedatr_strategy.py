import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'ModifiedATR': 1.0
        })
    )
