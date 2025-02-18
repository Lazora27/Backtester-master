import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
