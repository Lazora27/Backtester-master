import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
