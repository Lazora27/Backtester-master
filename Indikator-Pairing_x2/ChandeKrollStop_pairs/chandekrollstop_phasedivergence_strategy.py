import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'PhaseDivergence': 1.0
        })
    )
