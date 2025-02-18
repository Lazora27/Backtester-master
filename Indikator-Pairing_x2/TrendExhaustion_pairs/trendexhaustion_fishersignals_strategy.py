import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und FisherSignals
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'FisherSignals': 1.0
        })
    )
