import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
