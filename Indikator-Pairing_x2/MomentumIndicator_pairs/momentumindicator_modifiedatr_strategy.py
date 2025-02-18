import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'ModifiedATR': 1.0
        })
    )
