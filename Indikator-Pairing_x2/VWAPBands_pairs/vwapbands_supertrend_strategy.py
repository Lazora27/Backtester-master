import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und SuperTrend
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'SuperTrend': 1.0
        })
    )
