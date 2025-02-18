import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
