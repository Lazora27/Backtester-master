import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
