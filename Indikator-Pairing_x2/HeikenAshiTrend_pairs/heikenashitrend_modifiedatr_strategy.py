import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'ModifiedATR': 1.0
        })
    )
