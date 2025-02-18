import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
