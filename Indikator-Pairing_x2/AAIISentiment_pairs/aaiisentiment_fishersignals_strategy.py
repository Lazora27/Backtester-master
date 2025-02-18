import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'FisherSignals': 1.0
        })
    )
