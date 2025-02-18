import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'AccelerationBands': 1.0
        })
    )
