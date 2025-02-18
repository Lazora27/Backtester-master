import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'ModifiedATR': 1.0
        })
    )
