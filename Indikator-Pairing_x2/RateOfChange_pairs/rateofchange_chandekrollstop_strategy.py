import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
