import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
