import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
