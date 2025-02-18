import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'ModifiedATR': 1.0
        })
    )
