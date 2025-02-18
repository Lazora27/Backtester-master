import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ModifiedATR': 1.0
        })
    )
