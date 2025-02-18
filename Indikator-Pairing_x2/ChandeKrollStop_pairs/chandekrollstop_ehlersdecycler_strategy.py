import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'EhlersDecycler': 1.0
        })
    )
