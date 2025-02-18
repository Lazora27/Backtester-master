import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'BradleySiderograph': 1.0
        })
    )
