import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'EhlersDecycler': 1.0
        })
    )
