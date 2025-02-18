import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
