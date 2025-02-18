import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
