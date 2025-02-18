import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
