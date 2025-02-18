import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
