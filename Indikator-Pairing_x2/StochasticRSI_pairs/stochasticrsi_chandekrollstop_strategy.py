import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
