import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
