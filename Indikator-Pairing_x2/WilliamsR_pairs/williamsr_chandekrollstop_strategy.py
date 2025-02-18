import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
