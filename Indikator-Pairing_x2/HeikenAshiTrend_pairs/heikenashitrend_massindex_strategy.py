import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und MassIndex
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'MassIndex': 1.0
        })
    )
