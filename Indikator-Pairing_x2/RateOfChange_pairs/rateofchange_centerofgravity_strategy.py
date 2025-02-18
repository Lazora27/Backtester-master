import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'CenterOfGravity': 1.0
        })
    )
