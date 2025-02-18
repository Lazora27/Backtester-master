import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'ModifiedATR': 1.0
        })
    )
