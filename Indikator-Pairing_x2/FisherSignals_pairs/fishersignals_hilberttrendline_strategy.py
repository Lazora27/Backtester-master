import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'HilbertTrendline': 1.0
        })
    )
