import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'ModifiedATR': 1.0
        })
    )
