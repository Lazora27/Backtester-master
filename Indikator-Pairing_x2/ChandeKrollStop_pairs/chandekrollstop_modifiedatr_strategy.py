import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'ModifiedATR': 1.0
        })
    )
