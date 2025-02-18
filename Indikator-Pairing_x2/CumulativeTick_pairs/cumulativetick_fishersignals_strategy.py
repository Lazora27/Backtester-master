import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und FisherSignals
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'FisherSignals': 1.0
        })
    )
