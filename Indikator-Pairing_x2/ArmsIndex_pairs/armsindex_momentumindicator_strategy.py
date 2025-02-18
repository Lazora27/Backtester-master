import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'MomentumIndicator': 1.0
        })
    )
