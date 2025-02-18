import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AbsoluteBreadthIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AbsoluteBreadthIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AbsoluteBreadthIndex': {
                'class': AbsoluteBreadthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AbsoluteBreadthIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AbsoluteBreadthIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
