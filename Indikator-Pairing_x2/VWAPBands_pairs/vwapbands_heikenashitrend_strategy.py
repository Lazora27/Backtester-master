import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
