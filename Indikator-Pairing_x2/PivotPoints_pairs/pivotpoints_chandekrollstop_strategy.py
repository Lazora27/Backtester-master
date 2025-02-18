import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
