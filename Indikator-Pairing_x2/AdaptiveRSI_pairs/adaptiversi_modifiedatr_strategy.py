import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'ModifiedATR': 1.0
        })
    )
