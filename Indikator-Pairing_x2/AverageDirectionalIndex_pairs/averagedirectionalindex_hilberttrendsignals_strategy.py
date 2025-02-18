import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
