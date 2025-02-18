import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
