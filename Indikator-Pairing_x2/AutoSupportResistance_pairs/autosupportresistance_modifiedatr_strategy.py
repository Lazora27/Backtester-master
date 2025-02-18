import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ModifiedATR': 1.0
        })
    )
