import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
