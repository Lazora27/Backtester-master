import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und FisherSignals
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'FisherSignals': 1.0
        })
    )
