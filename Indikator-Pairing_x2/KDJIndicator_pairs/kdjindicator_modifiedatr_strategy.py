import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'ModifiedATR': 1.0
        })
    )
