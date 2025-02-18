import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'CoppockCurve': 1.0
        })
    )
