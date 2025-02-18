import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
