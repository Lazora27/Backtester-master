import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
