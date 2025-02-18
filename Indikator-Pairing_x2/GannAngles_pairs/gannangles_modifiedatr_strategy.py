import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'ModifiedATR': 1.0
        })
    )
