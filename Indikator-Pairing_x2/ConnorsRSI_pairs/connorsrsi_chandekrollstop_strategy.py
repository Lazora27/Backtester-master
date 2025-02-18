import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
