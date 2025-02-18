import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und WilliamsR
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'WilliamsR': 1.0
        })
    )
