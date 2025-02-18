import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'CoppockCurve': 1.0
        })
    )
