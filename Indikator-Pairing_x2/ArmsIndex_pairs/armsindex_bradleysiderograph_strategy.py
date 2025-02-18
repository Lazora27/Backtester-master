import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
