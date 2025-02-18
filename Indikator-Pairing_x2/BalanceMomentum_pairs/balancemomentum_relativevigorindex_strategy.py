import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
