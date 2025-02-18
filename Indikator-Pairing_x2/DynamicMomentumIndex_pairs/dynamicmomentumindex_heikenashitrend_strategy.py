import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
