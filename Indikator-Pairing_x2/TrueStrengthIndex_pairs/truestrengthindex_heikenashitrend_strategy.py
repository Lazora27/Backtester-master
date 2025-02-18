import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
