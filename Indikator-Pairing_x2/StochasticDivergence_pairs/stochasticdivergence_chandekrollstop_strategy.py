import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
