import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
