import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'DonchianVolatility': 1.0
        })
    )
