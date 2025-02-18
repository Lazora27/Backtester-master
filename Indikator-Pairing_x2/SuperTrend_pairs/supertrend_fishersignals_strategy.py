import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und FisherSignals
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'FisherSignals': 1.0
        })
    )
