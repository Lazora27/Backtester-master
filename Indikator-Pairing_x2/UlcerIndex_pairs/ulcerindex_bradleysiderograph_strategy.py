import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
