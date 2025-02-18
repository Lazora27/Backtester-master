import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'HilbertTrendline': 1.0
        })
    )
