import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
