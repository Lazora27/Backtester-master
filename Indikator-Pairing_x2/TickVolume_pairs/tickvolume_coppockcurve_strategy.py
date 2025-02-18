import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'CoppockCurve': 1.0
        })
    )
