import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'CenterOfGravity': 1.0
        })
    )
