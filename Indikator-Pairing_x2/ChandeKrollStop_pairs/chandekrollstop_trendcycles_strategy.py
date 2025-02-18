import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'TrendCycles': 1.0
        })
    )
