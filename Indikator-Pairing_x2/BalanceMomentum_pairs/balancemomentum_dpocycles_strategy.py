import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und DPOCycles
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'DPOCycles': 1.0
        })
    )
