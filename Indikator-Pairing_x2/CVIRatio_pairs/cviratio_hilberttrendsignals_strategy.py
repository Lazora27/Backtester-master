import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
