import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'CenterOfGravity': 1.0
        })
    )
