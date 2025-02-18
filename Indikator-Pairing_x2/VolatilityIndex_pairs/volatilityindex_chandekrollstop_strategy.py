import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
