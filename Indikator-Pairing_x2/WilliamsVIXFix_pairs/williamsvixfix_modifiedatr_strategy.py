import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'ModifiedATR': 1.0
        })
    )
