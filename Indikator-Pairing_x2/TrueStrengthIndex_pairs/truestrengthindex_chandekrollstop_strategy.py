import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
