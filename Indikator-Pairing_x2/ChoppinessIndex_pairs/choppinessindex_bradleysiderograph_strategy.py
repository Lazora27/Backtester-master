import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
