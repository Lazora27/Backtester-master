import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ModifiedATR': 1.0
        })
    )
