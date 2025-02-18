import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'CenterOfGravity': 1.0
        })
    )
