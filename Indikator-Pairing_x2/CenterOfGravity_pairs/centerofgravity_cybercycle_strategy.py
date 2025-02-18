import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und CyberCycle
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'CyberCycle': 1.0
        })
    )
