import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_LaggingVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und LaggingVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'LaggingVolatilityIndex': {
                'class': LaggingVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LaggingVolatilityIndex'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'LaggingVolatilityIndex': 1.0
        })
    )
