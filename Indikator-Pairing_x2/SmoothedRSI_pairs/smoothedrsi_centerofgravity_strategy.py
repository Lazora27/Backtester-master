import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'CenterOfGravity': 1.0
        })
    )
