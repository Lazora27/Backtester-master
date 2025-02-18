import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'ModifiedATR': 1.0
        })
    )
