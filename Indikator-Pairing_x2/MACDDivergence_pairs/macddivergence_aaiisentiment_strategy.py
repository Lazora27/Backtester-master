import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AAIISentiment': 1.0
        })
    )
