import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'BradleySiderograph': 1.0
        })
    )
