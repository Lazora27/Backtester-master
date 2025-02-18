import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
