import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
