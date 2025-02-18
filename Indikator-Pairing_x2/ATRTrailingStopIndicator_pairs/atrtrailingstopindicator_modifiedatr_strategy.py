import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ATRTrailingStopIndicator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ATRTrailingStopIndicator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'ATRTrailingStopIndicator': {
                'class': ATRTrailingStopIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ATRTrailingStopIndicator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'ATRTrailingStopIndicator': 1.0,
            'ModifiedATR': 1.0
        })
    )
